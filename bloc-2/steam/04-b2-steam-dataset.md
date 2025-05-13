# Helper code
Code pour récupérer localement le dataset:
```python
import boto3
from botocore import UNSIGNED
from botocore.config import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

s3.download_file('full-stack-bigdata-datasets', "Big_Data/Project_Steam/steam_game_output.json", "steam_game_output.json")
```

# Record sample
Extrait d'un enregistrement du dataset, le premier en l'occurence:

```json
{
  "id": "10",
  "data": {
    "appid": 10,
    "name": "Counter-Strike",
    "short_description": "Play the world's number 1 online action game. Engage in an incredibly realistic brand of terrorist warfare in this wildly popular team-based game. Ally with teammates to complete strategic missions. Take out enemy sites. Rescue hostages. Your role affects your team's success. Your team's success affects your role.",
    "developer": "Valve",
    "publisher": "Valve",
    "genre": "Action",
    "tags": {
      "Action": 5426,
      "FPS": 4831,
      "Multiplayer": 3392,
      "Shooter": 3353,
      "Classic": 2784,
      "Team-Based": 1864,
      "First-Person": 1707,
      "Competitive": 1607,
      "Tactical": 1344,
      "e-sports": 1192,
      "1990's": 1191,
      "PvP": 881,
      "Old School": 769,
      "Military": 632,
      "Strategy": 614,
      "Survival": 304,
      "Score Attack": 289,
      "1980s": 266,
      "Assassin": 227,
      "Nostalgia": 131
    },
    "type": "game",
    "categories": [
      "Multi-player",
      "Valve Anti-Cheat enabled",
      "Online PvP",
      "Shared/Split Screen PvP",
      "PvP"
    ],
    "owners": "10,000,000 .. 20,000,000",
    "positive": 201215,
    "negative": 5199,
    "price": "999",
    "initialprice": "999",
    "discount": "0",
    "ccu": 13990,
    "languages": "English, French, German, Italian, Spanish - Spain, Simplified Chinese, Traditional Chinese, Korean",
    "platforms": {
      "windows": true,
      "mac": true,
      "linux": true
    },
    "release_date": "2000/11/1",
    "required_age": 0,
    "website": "",
    "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/10/header.jpg?t=1666823513"
  }
}
```
