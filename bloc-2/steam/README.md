# Projet Steam's videogames platform

> [Présentation du projet sur Julie (JEDHA)](https://app.jedha.co/course/project-steam-ft/steam-ft)

## 🚧 Contexte du projet 

Dans le cadre de ce projet, nous nous plaçons dans la peau d’un(e) analyste travaillant pour Ubisoft, éditeur français de jeux vidéo. L’entreprise envisage de lancer un nouveau jeu vidéo révolutionnaire et souhaite, en amont, mieux comprendre l’écosystème actuel du jeu vidéo.

Pour cela, elle a demandé une analyse globale des jeux disponibles sur la plateforme Steam, afin d’identifier les tendances du marché, les préférences des joueurs et les facteurs qui influencent le succès ou la rentabilité d’un jeu.

## 📊 Objectifs d’analyses

L’analyse des jeux disponibles sur Steam pourra se décliner en plusieurs niveaux, afin d’offrir une vision globale et détaillée du marché :

### Analyse macro

* Quels sont les éditeurs ayant publié le plus de jeux sur Steam ?
* Quels sont les jeux les mieux notés ?
* Y a-t-il des années avec un nombre plus élevé de sorties ? La pandémie de Covid a-t-elle eu un impact sur le volume de publications ?
* Comment les prix sont-ils répartis ? Y a-t-il beaucoup de jeux en promotion ?
* Quelles sont les langues les plus représentées ?
* Combien de jeux sont interdits aux moins de 16 ou 18 ans ?

### Analyse par genre

* Quels sont les genres les plus représentés sur la plateforme ?
* Certains genres présentent-ils de meilleurs ratios d’avis positifs/négatifs ?
* Certains éditeurs privilégient-ils des genres particuliers ?
* Quels sont les genres les plus lucratifs ?

### Analyse par plateforme

* La majorité des jeux sont-ils disponibles sur Windows, Mac ou Linux ?
* Certains genres sont-ils plus souvent disponibles sur certaines plateformes ?

## 📁 Source des données

Le jeu de données utilisé pour cette analyse est disponible dans un bucket S3 à l’adresse suivante :
`s3://full-stack-bigdata-datasets/Big_Data/Project_Steam/steam_game_output.json`

Ce fichier au format **JSON** contient des données semi-structurées issues de la plateforme **Steam**, incluant des informations sur les jeux, les éditeurs, les genres, les plateformes, les avis utilisateurs, les prix, les langues, et bien plus encore.

## 🧾 Description du jeu de données

Le fichier `steam_game_output.json` contient des données semi-structurées au format JSON, avec une **structure imbriquée**. Chaque enregistrement représente un jeu disponible sur la plateforme Steam, avec les attributs suivants (liste non exhaustive) :

### 🔹 Attributs principaux

Un [extrait](04-b2-steam-dataset.md) du dataset permet de visualiser l'aspect du contenu.
Une recherche sur les data Steam permet d'en déduire les définitions suivantes:

* `appid` : Identifiant unique du jeu
* `name` : Nom du jeu
* `release_date` : Date de sortie du jeu
* `publisher` : Éditeur(s) du jeu (peut être une liste)
* `developer` : Développeur(s) du jeu
* `platforms` : Plateformes disponibles (Windows, Mac, Linux)
* `genre` : Genres du jeu (souvent plusieurs par jeu)
* `categories` : Fonctions ou modes de jeu (solo, multi, coop, etc.)
* `price` : Prix initial du jeu (en cents - USD -)
* `discount` : Promotion
* `required_age` : Âge minimum requis (0 si pout tout le monde)
* `languages` : Langues disponibles (liste séparée par une virgule)
* `positive` / `negative` : Nombre d’avis positifs et négatifs
* `owners` : Fourchette estimée du nombre de possesseurs
* `header_image` : URL vers l’image d’en-tête du jeu
* `ccu` : Number of concurrent users ?
* `initialprice` : Prix initial ?
* `short_description`: Courte description du jeu
* `tags`: Tags
* `type`: Type du produit (`hardware` ou `game`)
* `website` : Website du jeu

### 🔹 Données imbriquées

Certains champs sont des listes ou objets complexes, par exemple :

* `genre` et `categories` sont souvent sous forme de tableaux d’objets contenant des identifiants et des noms.
* `languages` peut inclure du texte formaté nécessitant du nettoyage ou une extraction de langue(s).
* `tags` est une structure dont les propriétés représentent un tag (son nom) et leur valeur le nombre de fois ou ce tag a été associé

Il est recommandé d’utiliser des fonctions comme `explode()`, `getField()`, ou encore des expressions régulières pour exploiter ces données efficacement avec **PySpark**.


## Structure du projet
[Powerpoint du projet Steam](https://1drv.ms/p/c/e238927bf76c9315/ET81F6nhhU9Ks0XiQK0Vd7IBk9WaYg2pUmp74HdUFLRYaA?e=xGkHF1)

Délivrables:
- [Published Databricks Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3677905065488226/3069174859939844/4660714707946372/latest.html): version publique du notebook databricks (disponible jusqu'à début Novembre 2025).
- [01-b2-steam-databricks-notebook-01.ipynb](01-b2-steam-databricks-notebook-01.ipynb): Le notebook utilisable sur Databricks (il n'est pas adapté pour une utilisation locale)
- [02-b2-steam-databricks.md](02-b2-steam-databricks.md): un résumé sur les délivrables
- [03-b2-steam-databricks-export-01.html](03-b2-steam-databricks-export-01.html): export HTML du notebook
