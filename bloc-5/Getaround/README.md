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





## Objectifs


---

Souhaites-tu également une version en anglais pour compléter le README en bilingue ?



Voici une version enrichie de ton texte, incluant une **présentation de la société Getaround** en introduction, et toujours structurée en deux sections principales : **Contexte** et **Objectifs**, en français.

---

## Présentation

**Getaround** est souvent décrit comme le **Airbnb de la voiture** : la plateforme permet de louer un véhicule auprès d’un particulier, pour quelques heures ou plusieurs jours. Fondée en 2009, la société a connu une croissance rapide. En 2019, elle comptait plus de **5 millions d’utilisateurs** et environ **20 000 voitures disponibles** dans le monde.

Partenaire de Jedha, Getaround propose à travers ce projet un **cas d’étude réaliste et stimulant**, inspiré de problématiques concrètes rencontrées en 2017.

---

## Contexte

Lors de la location d’un véhicule via Getaround, les utilisateurs effectuent un **check-in** au début et un **check-out** à la fin de la location. Ces étapes permettent de :

* Signaler les éventuels dommages (anciens ou nouveaux),
* Comparer les niveaux de carburant,
* Enregistrer le nombre de kilomètres parcourus.

Trois types de processus existent :

* 📱 Contrat numérique signé sur le smartphone du propriétaire,
* 🔓 Accès sans contact via l’application mobile (Getaround Connect),
* 📝 Contrat papier (cas très rare).

Il arrive que les conducteurs rendent le véhicule en **retard**, ce qui pose problème si une autre location est prévue peu après. Cela peut générer des **insatisfactions client** (attente, annulation, etc.) et mobiliser le **service client**.

---

## Objectifs

Pour limiter ces désagréments, l’équipe produit envisage d’imposer un **délai minimum entre deux locations**. Toutefois, cela pourrait **réduire la visibilité** des véhicules sur la plateforme, et donc **impacter les revenus** des propriétaires.

Ce projet vise à aider les équipes produit et data à prendre une décision éclairée en :

* Mesurant la part de revenus et de locations potentiellement affectés,
* Évaluant la fréquence des retards et leurs impacts réels,
* Testant différents scénarios (seuils, périmètres comme "Connect only").

Deux livrables sont attendus :

1. 🧾 Un **dashboard interactif** pour explorer les données et appuyer les décisions métier.
2. 🤖 Une **API avec un endpoint `/predict`**, utilisant un modèle de Machine Learning pour proposer des prix optimisés, accompagnée d’une documentation accessible via `/docs`.

---

Souhaite-tu également que je t’aide à structurer ce README complet avec un sommaire, les instructions d’exécution ou les dépendances du projet ?
