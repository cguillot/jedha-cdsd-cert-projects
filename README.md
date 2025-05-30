# Certification CDSD : Concepteur développeur en science des données

# Blocs
- [Bloc 1](bloc-1/README.md) : Construction et alimentation d'une infrastructure de gestion de données
- [Bloc 2](bloc-2/README.md) : Analyse exploratoire, descriptive et inférentielle de données
- [Bloc 3](bloc-3/README.md) : Analyse prédictive de données structurées par l'intelligence artificielle
- [Bloc 4](bloc-4/README.md) : Analyse prédictive de données non-structurées par l'intelligence artificielle
- [Bloc 5](bloc-5/README.md) : Industrialisation d'un algorithme d'apprentissage automatique et automatisation des processus de décision
- [Bloc 6](bloc-6/README.md) : Direction de projets de gestion de données

# Environement de développement

## Mise en place (facultatif pour de la lecture de notebook)
Il est impératif de configurer l'environnement et l'infrastructure partagés:

- [environnement](.env.sample): les variables d'environnement utilisées par les différents projets (nécessaire en cas de run uniquement)
- [infrastructure](common/README.md): le provisionning d'élément d'infrastrucures communs à tous les projets (uniquement pour construire un nouvel environnement pour les projets en ayant besoin)

## Dev container
Un devcontainer est associé au repository.
Il est recommandé de l'utiliser (VSCode devrait le proposer automatiquement).

Sur mac il faudra peut-être enlever les lignes suivantes:
```json
  "runArgs": [
    "--gpus",
    "all"
  ]
```
