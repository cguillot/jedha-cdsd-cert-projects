import os

from typing import Union
from pydantic import BaseModel, Field
from typing import Literal, List

import pandas as pd

import pickle
import joblib

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Describing the API
description = """
# GetaroundRentalPriceSuggestion API Documentation

L'API GetaroundRentalPriceSuggestion vous permet de proposer le prix de location le plus juste pour votre véhicule au sein du service GetAround.\n

"""

tags_metadata = [
    {
        "name": "Rental price suggestion",
        "description": "Ce endpoint vous permet de connaitre le prix de location suggéré pour un ensemble donnée de véhicules"
    }
]

app = FastAPI(
    title="GetaroundRentalPriceSuggestion",
    description=description,
    version="1.0",
    openapi_tags=tags_metadata,
    contact={
        "name": "C. GUILLOT",
        "mail": "cguillot.abo@gmail.com",
    },
)

########################################################
# Preload model stuffs
preprocessor_path = os.getenv('CDSD_B5_GETAROUND_PREPROCESSOR_PATH', './model/getaround_preprocessor.pkl')
model_path = os.getenv('CDSD_B5_GETAROUND_MODEL_PATH', './model/getaround_model.joblib')

with open(preprocessor_path, "rb") as file:
    ml_preprocessor = pickle.load(file)

ml_model = joblib.load(model_path)

########################################################
# API data models
RENTAL_MODEL_KEY_TYPE = Literal["Citroën", "Peugeot", "PGO", "Renault", "Audi", "BMW", "Ford", "Mercedes", "Opel", "Porsche", "Volkswagen", "KIA Motors", "Alfa Romeo", "Ferrari", "Fiat", "Lamborghini", "Maserati", "Lexus", "Honda", "Mazda", "Mini", "Mitsubishi", "Nissan", "SEAT", "Subaru", "Suzuki", "Toyota", "Yamaha"]
RENTAL_FUEL_TYPE = Literal["diesel", "petrol", "hybrid_petrol", "electro"]
RENTAL_PAINT_COLOR_TYPE = Literal["black", "grey", "white", "red", "silver", "blue", "orange", "beige", "brown", "green"]
RENTAL_CAR_TYPE = Literal["convertible", "coupe", "estate", "hatchback", "sedan", "subcompact", "suv", "van"]

class RentalCarProperties(BaseModel):
    model_key: RENTAL_MODEL_KEY_TYPE = Field(..., description="Identifiant du modèle (ex: 'Citroën')")
    mileage: Union[int, float] = Field(..., description="Kilométrage du véhicule")
    engine_power: Union[int, float] = Field(..., description="Puissance du moteur en chevaux")
    fuel: RENTAL_FUEL_TYPE = Field(..., description="Type de carburant")
    paint_color: RENTAL_PAINT_COLOR_TYPE = Field(..., description="Couleur de la carrosserie")
    car_type: RENTAL_CAR_TYPE = Field(..., description="Type de voiture")
    private_parking_available: bool = Field(..., description="Parking privé disponible")
    has_gps: bool = Field(..., description="Le véhicule a un GPS")
    has_air_conditioning: bool = Field(..., description="Climatisation présente")
    automatic_car: bool = Field(..., description="Boîte automatique")
    has_getaround_connect: bool = Field(..., description="Système Getaround Connect installé")
    has_speed_regulator: bool = Field(..., description="Régulateur de vitesse présent")
    winter_tires: bool = Field(..., description="Pneus hiver installés")

class SuggestPriceRequest(BaseModel):
    data: List[RentalCarProperties] = Field(..., description="Liste des véhicules à évaluer")

# Default redirected to /docs
@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

# tags=["Price Predictions 💶💶💶"]

@app.post("/predict", summary="Prévoir un prix de location", response_description="Prix recommandés pour chaque véhicule", tags=["Rental price suggestion"])
def predict(suggestionRequest: SuggestPriceRequest):
    """
    Prédit les prix de location recommandés pour une ou plusieurs voitures.

    - **Input** : un objet JSON contenant une liste de voitures avec leurs caractéristiques.
    - **Output** : une liste de prix recommandés (un par voiture fournie).

    ### Exemple de payload :
    ```json
    {
      "data": [
        {
          "model_key": "Citroën",
          "mileage": 50000,
          "engine_power": 120,
          "fuel": "diesel",
          "paint_color": "black",
          "car_type": "sedan",
          "private_parking_available": true,
          "has_gps": true,
          "has_air_conditioning": true,
          "automatic_car": false,
          "has_getaround_connect": true,
          "has_speed_regulator": true,
          "winter_tires": false
        }
      ]
    }
    ```

    ### Exemple de réponse :
    ```json
    {
      "recommended_rental_prices": [42.5]
    }
    ```
    """

    requested_cars = [requested.dict() for requested in suggestionRequest.data]
    df = pd.DataFrame(requested_cars)

    preprocessed_data = ml_preprocessor.transform(df)
    suggested_prices = ml_model.predict(preprocessed_data)

    suggested_prices = [round(price, 2) for price in suggested_prices.tolist()]

    return {"recommended_rental_prices": suggested_prices}
