# Module 1 — Fondations : de la donnée au graphique

Ce dossier contient les données, notebooks et exercices du premier module de la formation [Data Mastery](https://datamastery.dev).

## Démarrage

Ouvrir un terminal et taper ces 3 commandes :

```bash
git clone https://github.com/Formation-Data-Mastery/data-mastery-1.1-premiers-pas.git
cd data-mastery-1.1-premiers-pas
uv sync
```

Ouvrir le projet dans VS Code :

```bash
code .
```

Puis lancer Claude Code dans le terminal intégré de VS Code :

```bash
claude
```

À partir de là, suivre les leçons sur le site.

## Contenu du dossier

| Dossier | Contenu |
|---------|---------|
| `data/` | Fichiers CSV utilisés dans les leçons |
| `notebooks/` | Notebooks créés en suivant les leçons |
| `notebooks/reference/` | Notebooks de référence (à consulter après avoir essayé) |
| `exercices/` | Exercices avec énoncé et correction |
| `output/` | Graphiques HTML générés |

### Données disponibles

| Fichier | Description | Lignes |
|---------|-------------|--------|
| `consommation_energie.csv` | Consommation électricité et gaz par bâtiment et zone (2023-2024) | ~2 600 |
| `production_industrielle.csv` | Production par ligne et équipe, avec défauts (2024) | ~1 500 |
| `capteurs_temperature.csv` | Relevés de capteurs IoT toutes les 15 minutes | ~500 |
| `export_gtc_brut.csv` | Export GTC annuel avec anomalies — utilisé dans le cas d'étude | ~2 600 |

### Notebooks de référence

| Notebook | Leçon |
|----------|-------|
| `notebooks/reference/01_explorer_les_donnees.ipynb` | Leçon 1.3 — Premier graphique |
| `notebooks/reference/04_comprendre_dialogue.ipynb` | Leçon 1.4 — Comprendre le dialogue |
| `notebooks/reference/05_cas_etude_energie.ipynb` | Cas d'étude — Énergie |

## Leçons sur le site

| # | Leçon | Durée |
|---|-------|-------|
| 1.1 | [Qu'est-ce que Claude Code ?](https://datamastery.dev/module-1/lecon-1-1-quest-ce-que-claude-code) | 30 min |
| 1.2 | [Installation](https://datamastery.dev/module-1/lecon-1-2-installation) | 45 min |
| 1.3 | [Premier graphique](https://datamastery.dev/module-1/lecon-1-3-premier-graphique) | 60 min |
| 1.4 | [Comprendre le dialogue](https://datamastery.dev/module-1/lecon-1-4-comprendre-le-dialogue) | 45 min |
| — | [Cas d'étude : énergie](https://datamastery.dev/module-1/cas-etude-premier-graphique-energie) | 60 min |

## Besoin d'aide ?

- **Erreur API 500** : erreur transitoire côté Anthropic. Patienter 30 secondes et relancer le même prompt.
- **Résultat inattendu** : demander à Claude Code "Reprends depuis le début" ou "Qu'est-ce qui n'a pas marché ?"
- **Exercices** : commencer par l'énoncé, puis comparer avec la correction
- **Installation** : la leçon 1.2 contient un guide de résolution des problèmes courants
