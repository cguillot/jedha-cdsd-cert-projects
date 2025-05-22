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
JEDHA_GETAROUND_DELAY_DATASET_CSV_URL = "https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx"
JEDHA_GETAROUND_PRICING_DATASET_CSV_URL = "https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv"

# Local project data path
LOCAL_GETAROUND_DELAY_DATASET_CSV_PATH = DATA_BASE_DIR / "get_around_delay_analysis.xlsx"
LOCAL_GETAROUND_PRICING_DATASET_CSV_PATH = DATA_BASE_DIR / "get_around_pricing_project.csv"

# Machine Learning assets
LOCAL_ML_PREPOCESSOR_PKL_PATH = "./assets/ml/preprocessor.pkl"
LOCAL_ML_LINEAR_REGRESSION_MODEL_JOBLIB_PATH = "./assets/ml/model_linear_regression.joblib"
LOCAL_ML_RIDGE_MODEL_JOBLIB_PATH = "./assets/ml/model_ridge.joblib"
LOCAL_ML_LASSO_MODEL_JOBLIB_PATH = "./assets/ml/model_lasso.joblib"
LOCAL_ML_RANDOM_FOREST_MODEL_JOBLIB_PATH = "./assets/ml/model_random_forest.joblib"
# XGBoost
LOCAL_ML_XGBOOST_PREPOCESSOR_PKL_PATH = "./assets/ml/preprocessor_xgboost.pkl"
LOCAL_ML_XGBOOST_MODEL_JOBLIB_PATH = "./assets/ml/model_xgboost.joblib"

# Enforce ML parent path esit
Path(LOCAL_ML_PREPOCESSOR_PKL_PATH).parent.mkdir(parents=True, exist_ok=True)

# secrets
__env = {
    **dotenv_values("../../.env")
}

secrets = {
    "AWS_ACCESS_KEY_ID": __env["CDSD_AWS_ACCESS_KEY_ID"],
    "AWS_ACCESS_KEY_SECRET": __env["CDSD_AWS_ACCESS_KEY_SECRET"]
}
