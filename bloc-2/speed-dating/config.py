from dotenv import dotenv_values
from pathlib import Path

# base DATA folder
DATA_BASE_DIR = Path.joinpath(Path.cwd(), 'data')

if not DATA_BASE_DIR.exists():
    DATA_BASE_DIR.mkdir()
    print(f"Created data folder at {DATA_BASE_DIR}")
else:
    print(f"Data folder: {DATA_BASE_DIR}")

# JEDHA original project data URL
JEDHA_SPEED_DATING_CSV_URL = "https://full-stack-assets.s3.eu-west-3.amazonaws.com/M03-EDA/Speed+Dating+Data.csv"
JEDHA_SPEED_DATING_DATA_EXPLANATIONS_URL = "https://full-stack-assets.s3.eu-west-3.amazonaws.com/M03-EDA/Speed+Dating+Data+Key.doc"

# Local project data path
LOCAL_SPEED_DATING_CSV_PATH = DATA_BASE_DIR / "Speed+Dating+Data.csv"
LOCAL_SPEED_DATING_DATA_EXPLANATIONS_PATH = DATA_BASE_DIR / "Speed+Dating+Data+Key.docx"
LOCAL_SPEED_DATING_DATA_EXPLANATIONS_MD_PATH = DATA_BASE_DIR / "Speed+Dating+Data+Key.md"

# Les couleurs pré-définies pour certains type de données
COLORS = {
    "man": "lightblue",
    "woman": "lightpink"
}
# secrets

__env = {
    **dotenv_values("../../.env")
}

S3_BUCKET_NAME=__env["CDSD_S3_BUCKET_NAME"]

POSTGRES_DB_URL=__env["B1_KAYAK_POSTGRES_DB_URL"]

secrets = {
    "OPENAI_API_KEY": __env["OPENAI_API_KEY"],
    "AWS_ACCESS_KEY_ID": __env["CDSD_AWS_ACCESS_KEY_ID"],
    "AWS_ACCESS_KEY_SECRET": __env["CDSD_AWS_ACCESS_KEY_SECRET"]
}
