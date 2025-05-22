# Projet Getaround

> [Présentation du projet sur Julie (JEDHA)](https://app.jedha.co/course/project-deployment-ft/getaround-analysis-ft)

## Présentation

**Getaround** est souvent décrit comme le **Airbnb de la voiture** : la plateforme permet de louer un véhicule auprès d’un particulier, pour quelques heures ou plusieurs jours. Fondée en 2009, la société a connu une croissance rapide. En 2019, elle comptait plus de **5 millions d’utilisateurs** et environ **20 000 voitures disponibles** dans le monde.

## 🚧 Contexte du projet 

Lors de la location d’un véhicule via Getaround, les utilisateurs effectuent un **check-in** au début et un **check-out** à la fin de la location. Ces étapes permettent d’évaluer l’état du véhicule, de comparer le niveau de carburant et de mesurer le kilométrage parcouru.

Trois types de processus existent :

* 📱 Contrat numérique signé sur le smartphone du propriétaire.
* 🔓 Accès sans contact via l’application mobile (Getaround Connect).
* 📝 Contrat papier (cas marginal).

Cependant, il arrive que les conducteurs retournent le véhicule en retard, ce qui peut perturber la location suivante — notamment lorsque deux locations sont programmées le même jour. Cela engendre des frictions pour les utilisateurs et le service client.

## 📊 Objectifs

Pour réduire ces situations, l’équipe produit envisage d’instaurer un **délai minimum entre deux locations**. Cela pourrait diminuer les cas de retard, mais aussi impacter les revenus des propriétaires. Le but est de **trouver le bon compromis**.

Le projet vise à :

* Analyser l’impact potentiel de cette fonctionnalité sur les revenus et les locations.
* Identifier la fréquence et les conséquences des retards de restitution.
* Évaluer l’efficacité de la mesure en fonction de différents seuils et périmètres (ex : seulement les voitures Connect).

Deux livrables sont attendus :

1. 🧾 Un **dashboard interactif** (Streamlit ou autre) pour explorer les données et guider la prise de décision produit.
2. 🤖 Un **endpoint API `/predict`** basé sur un modèle de Machine Learning pour optimiser les prix des locations, avec une documentation disponible à l’adresse `/docs`.

## 📁 Source des données

Deux datasets sont fournis afin de réaliser une analyse et de présenter un modèle entrainé à l'optimisation du prix des locations.

- [Delay Analysis](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx) 👈 Data Analysis
- [Pricing Optimization](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv) 👈 Machine Learning

## Structure du projet
[Powerpoint du projet Steam]()

Délivrables:
- Notebooks:
  - [00-b5-JEDHA-Getaround_analysis.ipynb](00-b5-JEDHA-Getaround_analysis.ipynb) : le sujet
  - [01-b5-Getaround-delay-analysis.ipynb](01-b5-Getaround-delay-analysis.ipynb) : l'analyse du dataset des locations
  - [02-b5-Getaround-pricing-optimization.ipynb](02-b5-Getaround-pricing-optimization.ipynb) : l'étude des modèles de prédiction du prix de location

- Applications:
  - [deploiement](apps/README.md)

- Services déployés:
  - API: https://huggingface.co/spaces/pikaBOUM/cdsd-bloc-5-getaround-api
  - DAshboard: https://huggingface.co/spaces/pikaBOUM/cdsd-bloc-5-getaround-dashboard
