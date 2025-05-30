# Liste des colonnes du jeu de données Speed Dating
all_documented_columns = [
    # Identificateurs
    "iid",           # ID unique du sujet
    "id",            # Numéro du sujet dans la vague
    "gender",        # Genre (0=Femme, 1=Homme)
    "idg",           # Numéro du sujet par genre
    "condtn",        # Condition (1=choix limité, 2=choix étendu)
    "wave",          # Numéro de la vague de l'événement (notation des préférences des waves 6,7,8,9 différente des autres - entre 1 et 10 au lieu de la distribution de 100 points)

    # Informations sur l'événement
    "round",         # Nombre de personnes rencontrées dans la vague
    "position",      # Numéro de station où le partenaire a été rencontré
    "positin1",      # Numéro de station de départ
    "order",         # Numéro du rendez-vous pendant la soirée
    "partner",       # ID du partenaire pendant la soirée
    "pid",           # Numéro iid du partenaire
    "match",         # Correspondance mutuelle (1=oui, 0=non)
    "int_corr",      # Corrélation entre les évaluations d'intérêt
    "samerace",      # Même race/ethnie (1=oui, 0=non)

    # Caractéristiques du partenaire (on devrait les retrouver pour iid == pid)
    "age_o",         # Âge du partenaire
    "race_o",        # Race/ethnie du partenaire
    "pf_o_att",      # Préférence déclarée du partenaire pour l'attractivité
    "pf_o_sin",      # Préférence déclarée du partenaire pour la sincérité
    "pf_o_int",      # Préférence déclarée du partenaire pour l'intelligence
    "pf_o_fun",      # Préférence déclarée du partenaire pour l'amusement
    "pf_o_amb",      # Préférence déclarée du partenaire pour l'ambition
    "pf_o_sha",      # Préférence déclarée du partenaire pour les intérêts communs
    "dec_o",         # Décision du partenaire pendant l'événement
    "attr_o",        # Évaluation par le partenaire pendant l'événement (attractivité)
    "sinc_o",        # Évaluation par le partenaire pendant l'événement (sincérité)
    "intel_o",       # Évaluation par le partenaire pendant l'événement (intelligence)
    "fun_o",         # Évaluation par le partenaire pendant l'événement (amusement)
    "amb_o",         # Évaluation par le partenaire pendant l'événement (ambition)
    "shar_o",        # Évaluation par le partenaire pendant l'événement (intérêts communs)
    "like_o",        # Évaluation par le partenaire pendant l'événement (appréciation)
    "prob_o",        # Évaluation par le partenaire pendant l'événement (probabilité)
    "met_o",         # Déjà rencontré par le partenaire

    # Informations personnelles
    "age",           # Âge
    "field",         # Domaine d'étude
    "field_cd",      # Code du domaine d'étude
    "undergra",      # Établissement universitaire
    "mn_sat",        # Score SAT médian
    "tuition",       # Frais de scolarité
    "race",          # Race/ethnie
    "imprace",       # Importance de la race/ethnie dans les rencontres
    "imprelig",      # Importance de la religion dans les rencontres
    "from",          # Origine
    "zipcode",       # Code postal
    "income",        # Revenu médian du ménage
    "goal",          # Objectif principal de participation
    "date",          # Fréquence de rendez-vous en général
    "go_out",        # Fréquence de sorties
    "career",        # Carrière envisagée
    "career_c",      # Code de carrière

    # Intérêts et activités
    "sports",        # Intérêt pour le sport
    "tvsports",      # Intérêt pour les sports à la télévision
    "exercise",      # Intérêt pour l'exercice physique
    "dining",        # Intérêt pour la restauration
    "museums",       # Intérêt pour les musées
    "art",           # Intérêt pour l'art
    "hiking",        # Intérêt pour la randonnée
    "gaming",        # Intérêt pour les jeux
    "clubbing",      # Intérêt pour les boîtes de nuit
    "reading",       # Intérêt pour la lecture
    "tv",            # Intérêt pour la télévision
    "theater",       # Intérêt pour le théâtre
    "movies",        # Intérêt pour le cinéma
    "concerts",      # Intérêt pour les concerts
    "music",         # Intérêt pour la musique
    "shopping",      # Intérêt pour le shopping
    "yoga",          # Intérêt pour le yoga

    # Attentes
    "exphappy",      # Bonheur attendu
    "expnum",        # Nombre de personnes intéressées attendu

    # Préférences et auto-évaluations (Temps 1)
    "attr1_1",       # Importance de l'attractivité (Temps 1)
    "sinc1_1",       # Importance de la sincérité (Temps 1)
    "intel1_1",      # Importance de l'intelligence (Temps 1)
    "fun1_1",        # Importance de l'amusement (Temps 1)
    "amb1_1",        # Importance de l'ambition (Temps 1)
    "shar1_1",       # Importance des intérêts communs (Temps 1)

    "attr4_1",       # Perception de ce que la plupart des personnes du même sexe recherchent: attractivité (T1)
    "sinc4_1",       # Perception de ce que la plupart des personnes du même sexe recherchent: sincérité (T1)
    "intel4_1",      # Perception de ce que la plupart des personnes du même sexe recherchent: intelligence (T1)
    "fun4_1",        # Perception de ce que la plupart des personnes du même sexe recherchent: amusement (T1)
    "amb4_1",        # Perception de ce que la plupart des personnes du même sexe recherchent: ambition (T1)
    "shar4_1",       # Perception de ce que la plupart des personnes du même sexe recherchent: intérêts communs (T1)

    "attr2_1",       # Perception de ce que le sexe opposé recherche: attractivité (T1)
    "sinc2_1",       # Perception de ce que le sexe opposé recherche: sincérité (T1)
    "intel2_1",      # Perception de ce que le sexe opposé recherche: intelligence (T1)
    "fun2_1",        # Perception de ce que le sexe opposé recherche: amusement (T1)
    "amb2_1",        # Perception de ce que le sexe opposé recherche: ambition (T1)
    "shar2_1",       # Perception de ce que le sexe opposé recherche: intérêts communs (T1)

    "attr3_1",       # Auto-évaluation: attractivité (T1)
    "sinc3_1",       # Auto-évaluation: sincérité (T1)
    "intel3_1",      # Auto-évaluation: intelligence (T1)
    "fun3_1",        # Auto-évaluation: amusement (T1)
    "amb3_1",        # Auto-évaluation: ambition (T1)

    "attr5_1",       # Perception de comment les autres vous perçoivent: attractivité (T1)
    "sinc5_1",       # Perception de comment les autres vous perçoivent: sincérité (T1)
    "intel5_1",      # Perception de comment les autres vous perçoivent: intelligence (T1)
    "fun5_1",        # Perception de comment les autres vous perçoivent: amusement (T1)
    "amb5_1",        # Perception de comment les autres vous perçoivent: ambition (T1)

    # Évaluations pendant l'événement (Scorecard)
    "dec",           # Décision (1=oui, 0=non)
    "attr",          # Évaluation: attractivité
    "sinc",          # Évaluation: sincérité
    "intel",         # Évaluation: intelligence
    "fun",           # Évaluation: amusement
    "amb",           # Évaluation: ambition
    "shar",          # Évaluation: intérêts communs
    "like",          # Appréciation globale
    "prob",          # Probabilité que l'autre dise oui
    "met",           # Déjà rencontré (1=oui, 2=non)

    # Mi-parcours de l'événement
    "match_es",      # Estimation du nombre de correspondances
    "attr1_s",       # Importance de l'attractivité (mi-parcours)
    "sinc1_s",       # Importance de la sincérité (mi-parcours)
    "intel1_s",      # Importance de l'intelligence (mi-parcours)
    "fun1_s",        # Importance de l'amusement (mi-parcours)
    "amb1_s",        # Importance de l'ambition (mi-parcours)
    "shar1_s",       # Importance des intérêts communs (mi-parcours)

    "attr3_s",       # Auto-évaluation: attractivité (mi-parcours)
    "sinc3_s",       # Auto-évaluation: sincérité (mi-parcours)
    "intel3_s",      # Auto-évaluation: intelligence (mi-parcours)
    "fun3_s",        # Auto-évaluation: amusement (mi-parcours)
    "amb3_s",        # Auto-évaluation: ambition (mi-parcours)

    # Suivi (Temps 2)
    "satis_2",       # Satisfaction globale
    "length",        # Opinion sur la durée (4 minutes)
    "numdat_2",      # Opinion sur le nombre de rendez-vous

    "attr7_2",       # Importance réelle dans les décisions: attractivité (T2)
    "sinc7_2",       # Importance réelle dans les décisions: sincérité (T2)
    "intel7_2",      # Importance réelle dans les décisions: intelligence (T2)
    "fun7_2",        # Importance réelle dans les décisions: amusement (T2)
    "amb7_2",        # Importance réelle dans les décisions: ambition (T2)
    "shar7_2",       # Importance réelle dans les décisions: intérêts communs (T2)

    "attr1_2",       # Importance de l'attractivité (T2)
    "sinc1_2",       # Importance de la sincérité (T2)
    "intel1_2",      # Importance de l'intelligence (T2)
    "fun1_2",        # Importance de l'amusement (T2)
    "amb1_2",        # Importance de l'ambition (T2)
    "shar1_2",       # Importance des intérêts communs (T2)

    "attr4_2",       # Perception de ce que la plupart des personnes du même sexe recherchent: attractivité (T2)
    "sinc4_2",       # Perception de ce que la plupart des personnes du même sexe recherchent: sincérité (T2)
    "intel4_2",      # Perception de ce que la plupart des personnes du même sexe recherchent: intelligence (T2)
    "fun4_2",        # Perception de ce que la plupart des personnes du même sexe recherchent: amusement (T2)
    "amb4_2",        # Perception de ce que la plupart des personnes du même sexe recherchent: ambition (T2)
    "shar4_2",       # Perception de ce que la plupart des personnes du même sexe recherchent: intérêts communs (T2)

    "attr2_2",       # Perception de ce que le sexe opposé recherche: attractivité (T2)
    "sinc2_2",       # Perception de ce que le sexe opposé recherche: sincérité (T2)
    "intel2_2",      # Perception de ce que le sexe opposé recherche: intelligence (T2)
    "fun2_2",        # Perception de ce que le sexe opposé recherche: amusement (T2)
    "amb2_2",        # Perception de ce que le sexe opposé recherche: ambition (T2)
    "shar2_2",       # Perception de ce que le sexe opposé recherche: intérêts communs (T2)

    "attr3_2",       # Auto-évaluation: attractivité (T2)
    "sinc3_2",       # Auto-évaluation: sincérité (T2)
    "intel3_2",      # Auto-évaluation: intelligence (T2)
    "fun3_2",        # Auto-évaluation: amusement (T2)
    "amb3_2",        # Auto-évaluation: ambition (T2)

    "attr5_2",       # Perception de comment les autres vous perçoivent: attractivité (T2)
    "sinc5_2",       # Perception de comment les autres vous perçoivent: sincérité (T2)
    "intel5_2",      # Perception de comment les autres vous perçoivent: intelligence (T2)
    "fun5_2",        # Perception de comment les autres vous perçoivent: amusement (T2)
    "amb5_2",        # Perception de comment les autres vous perçoivent: ambition (T2)

    # Suivi (Temps 3)
    "you_call",      # Nombre de correspondances contactées
    "them_cal",      # Nombre de correspondances qui ont contacté
    "date_3",        # Rendez-vous avec des correspondances (1=oui, 2=non)
    "numdat_3",      # Nombre de correspondances avec qui il y a eu un rendez-vous
    "num_in_3",      # Nombre de personnes intéressées lors du suivi 3

    "attr1_3",       # Importance de l'attractivité (T3)
    "sinc1_3",       # Importance de la sincérité (T3)
    "intel1_3",      # Importance de l'intelligence (T3)
    "fun1_3",        # Importance de l'amusement (T3)
    "amb1_3",        # Importance de l'ambition (T3)
    "shar1_3",       # Importance des intérêts communs (T3)

    "attr7_3",       # Importance réelle dans les décisions: attractivité (T3)
    "sinc7_3",       # Importance réelle dans les décisions: sincérité (T3)
    "intel7_3",      # Importance réelle dans les décisions: intelligence (T3)
    "fun7_3",        # Importance réelle dans les décisions: amusement (T3)
    "amb7_3",        # Importance réelle dans les décisions: ambition (T3)
    "shar7_3",       # Importance réelle dans les décisions: intérêts communs (T3)

    "attr4_3",       # Perception de ce que la plupart des personnes du même sexe recherchent: attractivité (T3)
    "sinc4_3",       # Perception de ce que la plupart des personnes du même sexe recherchent: sincérité (T3)
    "intel4_3",      # Perception de ce que la plupart des personnes du même sexe recherchent: intelligence (T3)
    "fun4_3",        # Perception de ce que la plupart des personnes du même sexe recherchent: amusement (T3)
    "amb4_3",        # Perception de ce que la plupart des personnes du même sexe recherchent: ambition (T3)
    "shar4_3",       # Perception de ce que la plupart des personnes du même sexe recherchent: intérêts communs (T3)

    "attr2_3",       # Perception de ce que le sexe opposé recherche: attractivité (T3)
    "sinc2_3",       # Perception de ce que le sexe opposé recherche: sincérité (T3)
    "intel2_3",      # Perception de ce que le sexe opposé recherche: intelligence (T3)
    "fun2_3",        # Perception de ce que le sexe opposé recherche: amusement (T3)
    "amb2_3",        # Perception de ce que le sexe opposé recherche: ambition (T3)
    "shar2_3",       # Perception de ce que le sexe opposé recherche: intérêts communs (T3)

    "attr3_3",       # Auto-évaluation: attractivité (T3)
    "sinc3_3",       # Auto-évaluation: sincérité (T3)
    "intel3_3",      # Auto-évaluation: intelligence (T3)
    "fun3_3",        # Auto-évaluation: amusement (T3)
    "amb3_3",        # Auto-évaluation: ambition (T3)

    "attr5_3",       # Perception de comment les autres vous perçoivent: attractivité (T3)
    "sinc5_3",       # Perception de comment les autres vous perçoivent: sincérité (T3)
    "intel5_3",      # Perception de comment les autres vous perçoivent: intelligence (T3)
    "fun5_3",        # Perception de comment les autres vous perçoivent: amusement (T3)
    "amb5_3",        # Perception de comment les autres vous perçoivent: ambition (T3)
]

"""
Colonnes permettant de décrire un participant lors de son inscription:
- informations personnelles
- intérêts et activités
- attentes
"""
participant_cols = [
    "iid",
    "age",
    "gender",
    "gender_label",
    "race",
    "race_label",
    "goal",
    "goal_label",
    "field",
    "field_cd",
    "field_cd_label",
    "undergra",
    "mn_sat",
    "tuition",
    "imprace",
    "imprelig",
    "from",
    "zipcode",
    "income",
    "date",
    "go_out",
    "career",
    "career_c",
    "career_c_label",
    "sports",
    "tvsports",
    "exercise",
    "dining",
    "museums",
    "art",
    "hiking",
    "gaming",
    "clubbing",
    "reading",
    "tv",
    "theater",
    "movies",
    "concerts",
    "music",
    "shopping",
    "yoga",
    "exphappy",
    "expnum",
    "attr1_1",
    "sinc1_1",
    "intel1_1",
    "fun1_1",
    "amb1_1",
    "shar1_1",
    "attr4_1",
    "sinc4_1",
    "intel4_1",
    "fun4_1",
    "amb4_1",
    "shar4_1",
    "attr2_1",
    "sinc2_1",
    "intel2_1",
    "fun2_1",
    "amb2_1",
    "shar2_1",
    "attr3_1",
    "sinc3_1",
    "intel3_1",
    "fun3_1",
    "amb3_1",

    "attr5_1",
    "sinc5_1",
    "intel5_1",
    "fun5_1",
    "amb5_1",

    "attr1_s",       # Importance de l'attractivité (mi-parcours)
    "sinc1_s",       # Importance de la sincérité (mi-parcours)
    "intel1_s",      # Importance de l'intelligence (mi-parcours)
    "fun1_s",        # Importance de l'amusement (mi-parcours)
    "amb1_s",        # Importance de l'ambition (mi-parcours)
    "shar1_s",       # Importance des intérêts communs (mi-parcours)"

    "attr3_2",       # Auto-évaluation: attractivité (T2)
    "sinc3_2",       # Auto-évaluation: sincérité (T2)
    "intel3_2",      # Auto-évaluation: intelligence (T2)
    "fun3_2",        # Auto-évaluation: amusement (T2)
    "amb3_2",        # Auto-évaluation: ambition (T2)

    "attr7_2",       # Importance réelle dans les décisions: attractivité (T2)
    "sinc7_2",       # Importance réelle dans les décisions: sincérité (T2)
    "intel7_2",      # Importance réelle dans les décisions: intelligence (T2)
    "fun7_2",        # Importance réelle dans les décisions: amusement (T2)
    "amb7_2",        # Importance réelle dans les décisions: ambition (T2)
    "shar7_2",       # Importance réelle dans les décisions: intérêts communs (T2)

    "attr1_2",       # Importance de l'attractivité (T2)
    "sinc1_2",       # Importance de la sincérité (T2)
    "intel1_2",      # Importance de l'intelligence (T2)
    "fun1_2",        # Importance de l'amusement (T2)
    "amb1_2",        # Importance de l'ambition (T2)
    "shar1_2",       # Importance des intérêts communs (T2)

    "attr1_3",       # Importance de l'attractivité (T3)
    "sinc1_3",       # Importance de la sincérité (T3)
    "intel1_3",      # Importance de l'intelligence (T3)
    "fun1_3",        # Importance de l'amusement (T3)
    "amb1_3",        # Importance de l'ambition (T3)
    "shar1_3",       # Importance des intérêts communs (T3)

    "attr7_3",       # Importance réelle dans les décisions: attractivité (T3)
    "sinc7_3",       # Importance réelle dans les décisions: sincérité (T3)
    "intel7_3",      # Importance réelle dans les décisions: intelligence (T3)
    "fun7_3",        # Importance réelle dans les décisions: amusement (T3)
    "amb7_3",        # Importance réelle dans les décisions: ambition (T3)
    "shar7_3",       # Importance réelle dans les décisions: intérêts communs (T3)
]

pref_1_1_cols = ['attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1']
pref_4_1_cols = ['attr4_1', 'sinc4_1', 'intel4_1', 'fun4_1', 'amb4_1', 'shar4_1']
pref_2_1_cols = ['attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1']
pref_1_2_cols = ['attr1_2', 'sinc1_2', 'intel1_2', 'fun1_2', 'amb1_2', 'shar1_2']

####################################################
# Descriptive labels, from Speed+Dating+Data+Key.doc
####################################################
# race, race_o
race_labels = {
    1: "Black/African American",
    2: "European/Caucasian-American",
    3: "Latino/Hispanic American",
    4: "Asian/Pacific Islander/Asian-American",
    5: "Native American",
    6: "Other",
}

# field_cd
field_cd_labels = {
    1: "Law",
    2: "Math",
    3: "Social Science, Psychologist",
    4: "Medical Science, Pharmaceuticals, and Bio Tech",
    5: "Engineering",
    6: "English/Creative Writing/ Journalism",
    7: "History/Religion/Philosophy",
    8: "Business/Econ/Finance",
    9: "Education, Academia",
    10: "Biological Sciences/Chemistry/Physics",
    11: "Social Work",
    12: "Undergrad/undecided",
    13: "Political Science/International Affairs",
    14: "Film",
    15: "Fine Arts/Arts Administration",
    16: "Languages",
    17: "Architecture",
    18: "Other",
}

# gender
gender_labels = {
    0: "Woman", # Female
    1: "Man" # Male
}

# goal
goal_labels = {
    1: "Seemed like a fun night out",
    2: "To meet new people",
    3: "To get a date",
    4: "Looking for a serious relationship",
    5: "To say I did it",
    6: "Other",
}

# date
date_frequency_labels = {
    1: "Several times a week",
    2: "Twice a week",
    3: "Once a week",
    4: "Twice a month",
    5: "Once a month",
    6: "Several times a year",
    7: "Almost never",
}

# go_out
go_out_frequency_labels = {
    1: "Several times a week",
    2: "Twice a week",
    3: "Once a week",
    4: "Twice a month",
    5: "Once a month",
    6: "Several times a year",
    7: "Almost never",
}

# career_c
career_labels = {
    1: "Lawyer",
    2: "Academic/Research",
    3: "Psychologist",
    4: "Doctor/Medicine",
    5: "Engineer",
    6: "Creative Arts/Entertainment",
    7: "Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/Admin",
    8: "Real Estate",
    9: "International/Humanitarian Affairs",
    10: "Undecided",
    11: "Social Work",
    12: "Speech Pathology",
    13: "Politics",
    14: "Pro sports/Athletics",
    15: "Other",
    16: "Journalism",
    17: "Architecture",
}

attribute_labels = {
    "attr": "Attractive",
    "sinc": "Sincere",
    "intel": "Intelligent",
    "fun": "Fun",
    "amb": "Ambitious",
    "shar": "Shared Interests/Hobbies",
}

attribute_fast_labels = {
    "at": "Attractive",
    "si": "Sincere",
    "in": "Intelligent",
    "fu": "Fun",
    "am": "Ambitious",
    "sh": "Shared Interests/Hobbies",
}

# attr1_2 or attr_o
def get_attribute_label(attribute: str) -> str:
    if attribute is None:
        print("Expected attribute name, got None!")
        return None
    short_attr = attribute[:2]

    return attribute_fast_labels.get(short_attr)

class LabelDecoder():
    @staticmethod
    def get_attribute_label(attribute: str) -> str:
        if attribute is None:
            print("Expected attribute name, got None!")
            return None
        short_attr = attribute[:2]

        return attribute_fast_labels.get(short_attr)

    @staticmethod
    def get_race_label(race_id:int) -> str:
        if race_id is None:
            print("Expected race id, got None!")
            return None

        return race_labels.get(race_id)

    @staticmethod
    def get_gender_label(gender_id:int) -> str:
        if gender_id is None:
            print("Expected gender id, got None!")
            return None

        return gender_labels.get(gender_id)

    @staticmethod
    def get_career_label(career_id:int) -> str:
        if career_id is None:
            print("Expected career_id, got None!")
            return None

        return career_labels.get(career_id)


    @staticmethod
    def get_go_out_frequency_label(go_out_frequency_id:int) -> str:
        if go_out_frequency_id is None:
            print("Expected go_out_frequency_id, got None!")
            return None

        return go_out_frequency_labels.get(go_out_frequency_id)

    @staticmethod
    def get_date_frequency_label(date_frequency_id:int) -> str:
        if date_frequency_id is None:
            print("Expected date_frequency_id, got None!")
            return None

        return date_frequency_labels.get(date_frequency_id)

    @staticmethod
    def get_goal_label(goal_id:int) -> str:
        if goal_id is None:
            print("Expected goal_id, got None!")
            return None

        return goal_labels.get(goal_id)

    @staticmethod
    def get_field_cd_label(field_cd_id:int) -> str:
        if field_cd_id is None:
            print("Expected field_cd_id, got None!")
            return None

        return field_cd_labels.get(field_cd_id)

label_decoder = LabelDecoder()
