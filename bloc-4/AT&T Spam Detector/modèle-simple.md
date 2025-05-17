# **modèle simple** de classification spam / ham avec PyTorch

---

## 🧠 Objectif du modèle

Tu veux **classer un message texte** en deux classes :

* `0 = ham` (non-spam)
* `1 = spam`

Mais comme tu ne pars **pas d’un modèle de langage pré-entraîné**, tu vectorises les messages avec **TF-IDF** (chaque mot devient un score selon son importance dans le texte), et tu donnes ça comme **entrée à un réseau de neurones simple**.

---

## 🔍 Le modèle PyTorch

Voici le code du modèle :

```python
import torch.nn as nn

class SpamClassifier(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 2)  # 2 classes : ham et spam
        )

    def forward(self, x):
        return self.model(x)
```

---

## 🧱 Détail de l’architecture

### 1. **`nn.Linear(input_dim, 128)`**

* C’est une **couche dense** (fully connected)
* Elle transforme l’entrée (un vecteur TF-IDF de dimension `input_dim`, ex: 5000) en un vecteur de taille 128
* Elle apprend **des pondérations** pour chaque mot

### 2. **`nn.ReLU()`**

* Fonction d’activation : garde les valeurs positives, met les négatives à 0
* Ajoute de la **non-linéarité** → plus de capacité d’apprentissage

### 3. **`nn.Dropout(0.3)`**

* Pour éviter le surapprentissage (**drop 30%** des neurones pendant le training)

### 4. **`nn.Linear(128, 2)`**

* C’est la **couche de sortie**
* Elle produit un vecteur de taille 2 (1 score par classe)

> Ensuite, on utilise `CrossEntropyLoss` qui applique un **softmax + log-likelihood**, pour calculer la perte.

---

## 🔁 Forward Pass

* Le modèle prend un vecteur TF-IDF comme entrée (ex: `[0.1, 0.02, 0.0, ..., 0.4]`)
* Il le passe dans les couches
* Il retourne un **logit** (ex: `[1.4, 0.3]`)
* On prend `argmax` pour choisir la classe prédite

---

## 🎯 En résumé

| Élément            | Rôle                                                     |
| ------------------ | -------------------------------------------------------- |
| `TF-IDF`           | Transforme le texte en vecteur numérique                 |
| `Linear`           | Apprend à associer chaque mot à une classe               |
| `ReLU`             | Permet au réseau d’apprendre des relations non linéaires |
| `Dropout`          | Régularise pour éviter l’overfitting                     |
| `CrossEntropyLoss` | Calcule la perte entre prédiction et vérité              |

Excellente question ! Beaucoup se la posent en classification binaire.
Voici la **différence claire entre `BinaryCrossEntropy` et `CrossEntropyLoss`**, et **pourquoi on utilise `CrossEntropyLoss` ici** 👇

---

# BinaryCrossEntropy vs CrossEntropyLoss

## ✅ TL;DR

| Situation                    | Utilise             |
| ---------------------------- | ------------------- |
| 1 seule sortie (score spam)  | `BCEWithLogitsLoss` |
| 2 sorties (score ham + spam) | `CrossEntropyLoss`  |

---

## 🧠 Pourquoi tu utilises `CrossEntropyLoss`

Dans ton modèle :

```python
self.model = nn.Sequential(
    nn.Linear(input_dim, 128),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(128, 2)  # 🔹 2 sorties : ham et spam
)
```

→ **Tu as 2 sorties logiques** (`output = [score_ham, score_spam]`)

Tu veux que le modèle choisisse la classe avec le **score le plus élevé** ⇒ tu utilises :

```python
criterion = nn.CrossEntropyLoss()
```

✅ `CrossEntropyLoss` :

* Combine automatiquement **`log_softmax` + `negative log likelihood`**
* Prend des **logits** (non normalisés)
* S’attend à des **entiers comme labels** : `0` (ham), `1` (spam)

---

## ❓ Quand utiliser `BCEWithLogitsLoss` alors ?

Si tu fais une **classification binaire avec 1 seule sortie**, par exemple :

```python
self.model = nn.Sequential(
    nn.Linear(input_dim, 128),
    nn.ReLU(),
    nn.Linear(128, 1),  # 🔸 1 seule sortie : probabilité que ce soit du spam
)
```

→ Tu dois utiliser :

```python
criterion = nn.BCEWithLogitsLoss()
```

Et :

* La sortie doit passer par une **sigmoïde** (internement dans `BCEWithLogitsLoss`)
* Le label doit être un **float** entre `0.` et `1.`

---

## ✅ Résumé rapide

| Architecture               | Perte à utiliser      | Labels attendus |
| -------------------------- | --------------------- | --------------- |
| Sortie `nn.Linear(..., 2)` | `CrossEntropyLoss()`  | entiers `0/1`   |
| Sortie `nn.Linear(..., 1)` | `BCEWithLogitsLoss()` | float `0. / 1.` |

---

## 👉 Bonus : Multi-label ?

Si tu faisais de la **multi-label classification** (ex: un message peut être à la fois `spam` et `phishing`), alors tu aurais plusieurs sorties binaires → là aussi on utilise `BCEWithLogitsLoss`.

