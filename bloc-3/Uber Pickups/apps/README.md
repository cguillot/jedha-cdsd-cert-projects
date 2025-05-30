# Uber Rides Hot Zones dashboard

- Hot Zones dashboard: [/uber-hot-zones](./uber-hot-zones/README.md)

Déploiement via l'emploi du script [deploy.py](deploy.py).

La librairie d'assistance au déploiement vers huggingface est disponible ici: https://github.com/cguillot/jedha_infra_helpers.

```bash
uv run deploy.py --help

╭─ Commands ────────────────────────────────────────────────────────────╮
│ install   Deploy infrastructure                                       │
│ destroy   Destroy all deployed resources related to the deployment    │
╰───────────────────────────────────────────────────────────────────────╯
```

Pour le déploiement il est impératif d'avoir configuré les varaiables d'environnement relatives à huggingface (cf. [.env](../../../.env.sample)):
- CDSD_HUGGINGFACE_NAMESPACE: le nom du profil/espace huggingface à utiliser
- CDSD_HUGGINGFACE_TOKEN: un token d'accés en écriture à l'espace CDSD_HUGGINGFACE_NAMESPACE

Ensuite, pour tout déployer:
```bash
uv run deploy.py install
```
