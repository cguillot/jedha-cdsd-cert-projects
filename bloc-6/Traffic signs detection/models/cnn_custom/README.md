# Elaboration du modèle "Custom"

## Principe

Modèle "custom" de détection de panneaux.

**Principe** : Detection de formes géométriques + 1 cnn de décision "panneau ou non panneau" + 1 cnn de classification des panneaux

## Resources

* [makeModel1.ipynb](makeModel1.ipynb) : Entrainement du sous-modèle 1 de l'appeoche custom (Est-ce un panneau ?)

* [makeModel2.ipynb](makeModel2.ipynb) : Entrainement du sous-modèle 2 de l'appeoche custom (Classification des panneaux)

- [makeNonPanneaux.ipynb](makeNonPanneaux.ipynb) : Création aléatoire de "non panneaux" pour l'entrainement du sous modèle 1

- [data_prj.py](data_prj.py) : Fonctions partagées du projet  

- [panneaux](./panneaux) : Images des panneaux du périmètre de detection "brut"

- [panneaux_diff](./panneaux_diff) : Images de panneaux hors périmètre "brut"
