from dotenv import dotenv_values
from pathlib import Path

# base DATA folder
DATA_BASE_DIR = Path.joinpath(Path.cwd(), 'data')

if not DATA_BASE_DIR.exists():
    DATA_BASE_DIR.mkdir()
    print(f"Created data folder at {DATA_BASE_DIR}")
else:
    print(f"Data folder: {DATA_BASE_DIR}")

# destinations with geo locations CSV
CITIES_GEO_LOCATION_CSV_PATH = DATA_BASE_DIR / "cities_geo_locations.csv"

# weather forecast for all cities
CITIES_WEATHER_FORECAST_CSV_PATH = DATA_BASE_DIR / "cities_weather_forecast.csv"

# cities with geo location and weather related scores
CITIES_GEO_LOCATION_AND_SCORE_CSV_PATH = DATA_BASE_DIR / "cities_geo_locations_and_score.csv"

# best hotels per cities
BEST_HOTELS_OF_CITIES_JSON_PATH = DATA_BASE_DIR / "best_hotels_of_cities.json"

# secrets

__env = {
    **dotenv_values("../../.env")
}

# env = {
#     **dotenv_values("../../.env"),  # load shared development variables
#     #**dotenv_values(".env.shared"),  # load shared development variables
#     #**dotenv_values(".env.secret"),  # load sensitive variables
#     #**os.environ,  # override loaded values with environment variables
# }

# print(f"Env loaded: {config['ENV_NAME']}")
# #print(f"Env available: {config.keys()}")

# KAYAK_POSTGRES_DB_URL=config['KAYAK_POSTGRES_DB_URL']
# AWS_CGUILLOT_S3_KEY_ID=config['AWS_CGUILLOT_S3_KEY_ID']
# AWS_CGUILLOT_S3_KEY_SECRET=config['AWS_CGUILLOT_S3_KEY_SECRET']
# OPENWEATHERMAP_API_KEY=config['OPENWEATHERMAP_API_KEY']

S3_BUCKET_NAME=__env["CDSD_S3_BUCKET_NAME"]

POSTGRES_DB_URL=__env["B1_KAYAK_POSTGRES_DB_URL"]

secrets = {
    "OPENWEATHERMAP_API_KEY": __env["OPENWEATHERMAP_API_KEY"],
    "AWS_ACCESS_KEY_ID": __env["CDSD_AWS_ACCESS_KEY_ID"],
    "AWS_ACCESS_KEY_SECRET": __env["CDSD_AWS_ACCESS_KEY_SECRET"]
}
