# Getaround price suggestion API
## Présentation
Cette API fournit deux endpoints:
- `/docs`: la documentation interactive de l'API
- `/predict`: le endpoint de prédiction de prix

## Dévelopement

```bash
uv run fastapi dev
```

## Prediction endpoint

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
