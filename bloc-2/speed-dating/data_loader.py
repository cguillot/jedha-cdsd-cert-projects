import requests
import pandas as pd

from speed_dating_document_context import (
    LabelDecoder,
    pref_1_1_cols,
    pref_4_1_cols,
    pref_2_1_cols,
    pref_1_2_cols
)

from config import (
    JEDHA_SPEED_DATING_DATA_EXPLANATIONS_URL,
    LOCAL_SPEED_DATING_DATA_EXPLANATIONS_PATH,
    JEDHA_SPEED_DATING_CSV_URL,
    LOCAL_SPEED_DATING_CSV_PATH,
    # LOCAL_SPEED_DATING_DATA_EXPLANATIONS_MD_PATH
)

"""
    Function to load a cleaned dataset from within analysis notebooks
"""
def load_and_prepare_dataset():
    # Retrieve locally explanation document
    if not LOCAL_SPEED_DATING_DATA_EXPLANATIONS_PATH.exists():
        response = requests.get(JEDHA_SPEED_DATING_DATA_EXPLANATIONS_URL)

        with open(LOCAL_SPEED_DATING_DATA_EXPLANATIONS_PATH, mode="wb") as file:
            file.write(response.content)

    if not LOCAL_SPEED_DATING_CSV_PATH.exists():
        response = requests.get(JEDHA_SPEED_DATING_CSV_URL)

        with open(LOCAL_SPEED_DATING_CSV_PATH, mode="wb") as file:
            file.write(response.content)

    # Loading DataFrame
    speed_dating_df = pd.read_csv(LOCAL_SPEED_DATING_CSV_PATH, encoding="ISO-8859-1")

    # Drop some NA
    speed_dating_df.dropna(subset=["pid"], ignore_index=True, inplace=True)

    # enforce boundaries for abnormal values (could be a global sanitization applied on all columns expecting a range)
    abnormal_cols = ["attr_o", "fun_o", "gaming", "reading"]

    speed_dating_df[abnormal_cols] = speed_dating_df[abnormal_cols].clip(lower=1, upper=10)

    # Normalisation des notes

    waves_6_9_mask = speed_dating_df['wave'].between(6,9, inclusive='both')

    speed_dating_df[waves_6_9_mask] = speed_dating_df[waves_6_9_mask].apply(nomalize_wave_preferences, axis=1)

    # When numeric indexes, categorical columns can be converted to int
    id_columns = ["iid", "id", "idg", "wave", "position", "positin1", "order", "partner", "pid"]
    categorical_columns = ["gender", "condtn", "match", "dec", "dec_o", "samerace", "race", "race_o",
                        "field_cd", "goal", "go_out", "career_c", "date"]

    speed_dating_df[id_columns] = speed_dating_df[id_columns].astype('Int64')
    speed_dating_df[categorical_columns] = speed_dating_df[categorical_columns].astype('Int64')

    speed_dating_df["gender_label"] = speed_dating_df["gender"].map(LabelDecoder.get_gender_label)

    # Lisibilité
    # Gender
    speed_dating_df["gender_label"] = speed_dating_df["gender"].map(LabelDecoder.get_gender_label)

    # Race (race, race_o) Other = 6
    speed_dating_df.fillna({"race": 6}, inplace=True)
    speed_dating_df["race_label"] = speed_dating_df["race"].map(LabelDecoder.get_race_label)

    speed_dating_df.fillna({"race_o": 6}, inplace=True)
    speed_dating_df["race_label_o"] = speed_dating_df["race_o"].map(LabelDecoder.get_race_label)

    # # Goal (goal) Other = 6
    speed_dating_df.fillna({"goal": 6}, inplace=True)
    speed_dating_df["goal_label"] = speed_dating_df["goal"].map(LabelDecoder.get_goal_label)

    # # Field Coded (field_cd) Other = 18
    speed_dating_df.fillna({"field_cd": 18}, inplace=True)
    speed_dating_df["field_cd_label"] = speed_dating_df["field_cd"].map(LabelDecoder.get_field_cd_label)

    # Career (career_c) Other = 15
    speed_dating_df.fillna({"career_c": 15}, inplace=True)
    speed_dating_df["career_c_label"] = speed_dating_df["career_c"].map(LabelDecoder.get_career_label)

    return speed_dating_df

def nomalize_wave_preferences(row):
    # For all batch of preferences, rescale values to have sum() == 100
    for columns in [pref_1_1_cols, pref_4_1_cols, pref_2_1_cols, pref_1_2_cols]:
        preferences = row[columns]

        pref_total = preferences.sum()

        if pref_total > 0:
            # rescale pref_total -> 100
            def normalize_pref(p):
                if p is None:
                    return None

                return ((p / pref_total) * 100)

            row[columns] = preferences.apply(normalize_pref)

    return row
