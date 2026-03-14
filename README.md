# Module 1.1 — Premiers pas : de la donnée au graphique

> De la donnée brute au graphique exploitable en une session. Ce module pose les fondations : installation de l'environnement, premier contact avec Claude Code, et création de visualisations à partir de données industrielles réelles.

## Prérequis

- Un ordinateur (Mac, Windows ou Linux)
- Aucune expérience en programmation requise
- Avoir suivi les leçons 1 et 2 sur [datamastery.dev](https://datamastery.dev) (introduction + installation)

## Contenu

### Leçons sur le site

Les deux premières leçons sont des guides texte disponibles sur le site de la formation :

| # | Leçon | Durée | Description |
|---|-------|-------|-------------|
| 01 | [Introduction à Claude Code](https://datamastery.dev/module-1/lecon-1-1-quest-ce-que-claude-code) | 30 min | Comprendre l'agent, ses outils, et en quoi il diffère d'un chatbot |
| 02 | [Installation et configuration](https://datamastery.dev/module-1/lecon-1-2-installation) | 45 min | Terminal, VS Code, Node.js, Claude Code, Python, uv, Git |

### Notebooks

Les notebooks sont le support pratique — code exécutable, exemples concrets, visualisations. Les ouvrir dans VS Code (extension Jupyter).

| # | Notebook | Durée | Description |
|---|----------|-------|-------------|
| 03 | [Premier graphique](notebooks/03_premier_graphique.ipynb) | 60 min | Du CSV au graphique Plotly interactif — 5 exemples concrets |
| 04 | [Comprendre le dialogue](notebooks/04_comprendre_dialogue.ipynb) | 45 min | Architecture agent, outils, permissions, optimisation des instructions |
| 05 | [Cas d'étude : énergie industrielle](notebooks/05_cas_etude_energie.ipynb) | 60 min | 2 600 lignes de données GTC → 4 graphiques, 3 insights métier |

### Exercices

Chaque exercice existe en deux versions : l'énoncé (à compléter) et la correction.

| # | Exercice | Niveau | Durée |
|---|----------|--------|-------|
| 1 | Explorer un CSV ([énoncé](exercices/exercice_1_ENONCE.ipynb) / [correction](exercices/exercice_1_CORRECTION.ipynb)) | Débutant | 20 min |
| 2 | Créer 3 graphiques ([énoncé](exercices/exercice_2_ENONCE.ipynb) / [correction](exercices/exercice_2_CORRECTION.ipynb)) | Intermédiaire | 40 min |
| 3 | Analyse complète ([énoncé](exercices/exercice_3_ENONCE.ipynb) / [correction](exercices/exercice_3_CORRECTION.ipynb)) | Avancé | 60 min |

### Données

| Fichier | Lignes | Description |
|---------|--------|-------------|
| `data/consommation_energie.csv` | ~2 600 | Export GTC : consommation électricité/gaz par bâtiment et zone |
| `data/production_industrielle.csv` | ~1 500 | Production manufacturière : quantités, défauts, temps d'arrêt |
| `data/capteurs_temperature.csv` | ~500 | Capteurs IoT : température et humidité toutes les 15 minutes |

## Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/Formation-Data-Mastery/data-mastery-1.1-premiers-pas.git
cd data-mastery-1.1-premiers-pas

# Installer les dépendances
uv sync

# Ouvrir dans VS Code
code .
```

Puis ouvrir un notebook (`.ipynb`) depuis l'explorateur de fichiers de VS Code. Sélectionner le kernel Python du projet (`.venv`) quand VS Code le demande.

## Structure

```
1.1-Premiers-pas/
├── README.md
├── pyproject.toml
├── .python-version
├── .gitignore
│
├── notebooks/
│   ├── 03_premier_graphique.ipynb
│   ├── 04_comprendre_dialogue.ipynb
│   └── 05_cas_etude_energie.ipynb
│
├── exercices/
│   ├── exercice_1_ENONCE.ipynb
│   ├── exercice_1_CORRECTION.ipynb
│   ├── exercice_2_ENONCE.ipynb
│   ├── exercice_2_CORRECTION.ipynb
│   ├── exercice_3_ENONCE.ipynb
│   └── exercice_3_CORRECTION.ipynb
│
└── data/
    ├── consommation_energie.csv
    ├── production_industrielle.csv
    ├── capteurs_temperature.csv
    └── generate_data.py
```

## Licence

Ce contenu est la propriété de Data Mastery (datamastery.dev). Usage personnel et éducatif autorisé.
