# Module 1.1 — Premiers pas : de la donnée au graphique

> De la donnée brute au graphique exploitable en une session. Ce module pose les fondations : installation de l'environnement, premier contact avec Claude Code, et création de visualisations à partir de données industrielles réelles.

## Prérequis

- Un ordinateur (Mac, Windows ou Linux)
- Aucune expérience en programmation requise

## Contenu

### Notebooks

| # | Notebook | Durée | Description |
|---|----------|-------|-------------|
| 01 | [Introduction à Claude Code](notebooks/01_introduction_claude_code.ipynb) | 30 min | Comprendre l'agent, ses outils, et en quoi il diffère d'un chatbot |
| 02 | [Installation et configuration](notebooks/02_installation_configuration.ipynb) | 45 min | Terminal, Node.js, Claude Code, clé API, Python, uv |
| 03 | [Premier graphique](notebooks/03_premier_graphique.ipynb) | 60 min | Du CSV au graphique Plotly interactif — 5 exemples concrets |
| 04 | [Comprendre le dialogue](notebooks/04_comprendre_dialogue.ipynb) | 45 min | Architecture agent, outils, permissions, optimisation des instructions |
| 05 | [Cas d'étude : énergie industrielle](notebooks/05_cas_etude_energie.ipynb) | 60 min | 2 600 lignes de données GTC → 4 graphiques, 3 insights métier |

### Exercices

| # | Exercice | Niveau | Description |
|---|----------|--------|-------------|
| 1 | [Explorer un CSV](exercices/exercice_1_ENONCE.ipynb) | Débutant | Charger, explorer et décrire un jeu de données |
| 2 | [Créer 3 graphiques](exercices/exercice_2_ENONCE.ipynb) | Intermédiaire | Choisir et produire 3 visualisations pertinentes |
| 3 | [Analyse complète](exercices/exercice_3_ENONCE.ipynb) | Avancé | De la donnée brute au rapport avec graphiques et insights |

### Données

| Fichier | Lignes | Description |
|---------|--------|-------------|
| `data/consommation_energie.csv` | ~2 600 | Export GTC : consommation électricité/gaz par bâtiment et zone |
| `data/production_industrielle.csv` | ~1 500 | Production manufacturière : quantités, défauts, temps d'arrêt |
| `data/capteurs_temperature.csv` | ~500 | Capteurs IoT : température et humidité toutes les 15 minutes |

## Installation

### 1. Cloner le projet

```bash
git clone <repository-url>
cd Formation-Data-Mastery/1.1-Premiers-pas
```

### 2. Initialiser l'environnement avec uv

Si `uv` n'est pas installé, installer depuis [uv.astral.sh](https://github.com/astral-sh/uv).

```bash
uv sync
```

Cela crée un `.venv/` local et installe toutes les dépendances.

### 3. Activer l'environnement

```bash
source .venv/bin/activate
```

Ou sur Windows :

```bash
.venv\Scripts\activate
```

### 4. Lancer Jupyter Lab

```bash
jupyter lab
```

Accéder ensuite à `http://localhost:8888` dans le navigateur.

## Structure

```
1.1-Premiers-pas/
├── README.md                          # Ce fichier
├── pyproject.toml                     # Configuration Python uv
├── .python-version                    # Python 3.12
├── .gitignore                         # Fichiers ignorés par Git
│
├── notebooks/                         # Notebooks pédagogiques (screencasts)
│   ├── 01_introduction_claude_code.ipynb
│   ├── 02_installation_configuration.ipynb
│   ├── 03_premier_graphique.ipynb
│   ├── 04_comprendre_dialogue.ipynb
│   └── 05_cas_etude_energie.ipynb
│
├── exercices/                         # Énoncés et solutions
│   ├── exercice_1_ENONCE.ipynb
│   ├── exercice_1_SOLUTION.ipynb
│   ├── exercice_2_ENONCE.ipynb
│   ├── exercice_2_SOLUTION.ipynb
│   ├── exercice_3_ENONCE.ipynb
│   └── exercice_3_SOLUTION.ipynb
│
└── data/                              # CSV d'exemple
    ├── consommation_energie.csv
    ├── production_industrielle.csv
    └── capteurs_temperature.csv
```

## Licence

Ce contenu est la propriété de Data Mastery. Utilisation personnelle et éducative autorisée.
