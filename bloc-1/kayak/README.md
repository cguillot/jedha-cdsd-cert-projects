# Projet Kayak
## Présentation
### Contexte
L'équipe Marketing a fait deux constats à l’issu d'une étude utilisateur :
- 70 % des utilisateurs qui prévoient un voyage aimeraient plus d'informations sur leur destination.
- Les utilisateurs sont souvent sceptiques face aux contenus non liés à une marque reconnue.


### Demaande
L’équipe souhaite donc développer une application de recommandation de destinations de voyage.
A partir de données réelles, l’application recommandera les meilleures destinations et hôtels, en fonction :
- des conditions météorologiques
- de l’offre hôtelière disponible

## Structure du projet

Présentation du projet JEDHA:
- [00-JEDHA-Plan_your_trip_with_Kayak.ipynb](00-JEDHA-Plan_your_trip_with_Kayak.ipynb)

Configuration commune du projet
- [config.py](config.py): exporte les variables et secrets utilisés par les différents notebooks
- nécessite la mise en place de l'infrastructure commune:
  - [.env](../../.env.sample) à la racine du repository
  - [common infra](../../common/README.md)

Récupération (via l'APIs Nominatim) des coordonnées GPS des villes
- [01-b1-kayak-destinations.ipynb](01-b1-kayak-destinations.ipynb)
- résultats:
  - [cities_geo_locations.csv](data/cities_geo_locations.csv): liste des villes avec leurs coordonnées GPS

Récupération (via l'APIs OpenWeather) des prévisions météo des villes
- [02-b1-kayak-cities-weather-forecast.ipynb](02-b1-kayak-cities-weather-forecast.ipynb)
- [etl.py](etl.py): fonctions communes utilisées pour la transformation des données météos (ranking)
- résultats:
  - [cities_weather_forecast.csv](data/cities_weather_forecast.csv): prévisions météo à 5 jours par ville
  - [cities_geo_locations_and_score.csv](data/cities_geo_locations_and_score.csv): liste des villes avec leurs coordonnées GPS et leur ranking en fonction de la météo à venir

Récupération des meilleurs hotels pour chaque ville
- [scrapper](scrapper/README.md): projet scrapy pour le scraping de Booking.com
- [03-b1-kayak-get-hotels.ipynb](03-b1-kayak-get-hotels.ipynb): invocation du scraper dupuis un notebook
- [utils.py](utils.py): fonctions utilitaires
- résultats:
  - [best_hotels_of_cities.json](data/best_hotels_of_cities.json): liste des hotels avec leurs caractéristiques

Stockage vers Amazon S3 et transformation/stockage vers PostgreSQL
- [04-b1-kayak-etl.ipynb](04-b1-kayak-etl.ipynb)
- [etl.py](etl.py): fonctions communes utilisées pour la transformation des données météos (ranking)
- [utils.py](utils.py): fonctions utilitaires
- résultats:
  - ![s3_content_b1-kayak.png](assets/s3_content_b1-kayak.png)

Génération des cartes de recommendations
- [05-b1-kayak-viz.ipynb](05-b1-kayak-viz.ipynb)
- [utils.py](utils.py): fonctions utilitaires
- résultats:
  - table des villes: ![table des villes](assets/b1-kayak-neondb-cities.png)
  - table des hotels: ![table des hotels](assets/b1-kayak-neondb-hotels-of-city.png)
  - table du ranking des villes: ![table du ranking des villes](assets/b1-kayak-neondb-score-of-city.png)




