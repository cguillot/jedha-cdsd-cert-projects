# Projet Uber Pickups

> [Présentation du projet sur Julie (JEDHA)](https://app.jedha.co/course/projects-supervised-machine-learning-ft/walmart-sales-ft)

Voici une version traduite et légèrement raccourcie de la présentation :

## Présentation de l’entreprise 📇

Uber est l’une des startups les plus connues au monde. Lancée comme une application de covoiturage pour ceux qui ne pouvaient pas se permettre un taxi, elle a élargi ses services à la livraison de repas (Uber Eats), de colis, au transport de fret, et même à la mobilité urbaine avec Jump Bike et Lime.

L’ambition d’Uber est de révolutionner le transport à l’échelle mondiale. L’entreprise est désormais présente dans près de 70 pays et 900 villes, avec un chiffre d’affaires dépassant 14 milliards de dollars ! 😮

## Projet 🚧

Un problème identifié par Uber : parfois, il n’y a pas de chauffeurs là où les clients en ont besoin. Par exemple, un utilisateur dans le quartier financier de San Francisco peut devoir attendre 10 à 15 minutes alors que les chauffeurs se trouvent dans un autre quartier.

Or, les études montrent que les utilisateurs sont prêts à attendre 5 à 7 minutes maximum, au-delà, ils annulent souvent leur course.

Pour anticiper la demande, l’équipe data d’Uber souhaite recommander aux chauffeurs les zones "chaudes" à privilégier selon l’heure.

## Objectifs 🎯

À partir des données de courses existantes, votre mission est de :

* Développer un algorithme pour détecter les zones à forte demande.
* Visualiser les résultats dans un tableau de bord clair et interactif.


## 📁 Sources des données

- [dataset (zip)](https://full-stack-bigdata-datasets.s3.eu-west-3.amazonaws.com/Machine+Learning+non+Supervis%C3%A9/Projects/uber-trip-data.zip) : archive de plusieurs CSV

## Structure du projet

JEDHA:
- [00-b3-JEDHA-Uber_Pickups.ipynb](00-b3-JEDHA-Uber_Pickups.ipynb) : présentation du projet

Délivrables:
- [01-b3-Uber_Pickups_EDA](01-b3-Uber_Pickups_EDA.ipynb) : chargement des données et EDA
- [02-b3-Uber_Pickups_K-Means](02-b3-Uber_Pickups_K-Means.ipynb) : exploration clustering K-Means
- [03-b3-Uber_Pickups_DBSCAN](03-b3-Uber_Pickups_DBSCAN.ipynb) : exploration clustering DBSCAN
- [04-b3-Uber_Pickups_Generalisation](04-b3-Uber_Pickups_Generalisation.ipynb) : construction d'un graphe interactif pour les différent jours de la semaine
- [05-b3-Uber_Pickups_images.md](05-b3-Uber_Pickups_images.md) : inventaire des snapshots des graphiques du notebooks (ceux qui ne sont pas visibles dans github)

Live Hot Zones dashboard:
- [Uber Hot Zones - démo](https://pikaboum-cdsd-bloc-3-uber-rides-dashboard.hf.space/)

Présentation
- [PPT projet Uber Pickups](https://1drv.ms/p/c/e238927bf76c9315/EUzidAMyPTlBk698DPXLAJYBEeoNl3QmiQaIYoz-HYnVPQ?e=o5Zsq2)

## Wednesday hot zones animation

### Interactive hot-zones map
[wednesday's hot-zones](assets/wednesday_hot_zones.html)

### Animated GIF
![wednesday_hot_zones_animation](assets/wednesday_hot_zones_animation.gif)
