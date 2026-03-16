# Module 1 — Premiers pas : de la donnée au graphique

Ce dossier contient les données et exercices du premier module de la formation [Data Mastery](https://datamastery.dev).

## Comment suivre ce module

1. Ouvrir les leçons sur le site [datamastery.dev](https://datamastery.dev)
2. Suivre les instructions pas à pas
3. Taper les commandes et les prompts Claude Code soi-meme
4. Les fichiers de donnees sont dans le dossier `data/`

## Demarrage

Ouvrir un terminal et taper ces 4 commandes :

```bash
git clone https://github.com/Formation-Data-Mastery/data-mastery-1.1-premiers-pas.git
cd data-mastery-1.1-premiers-pas
uv sync
code .
```

Puis lancer Claude Code dans le terminal de VS Code :

```bash
claude
```

A partir de la, suivre les lecons sur le site.

## Contenu du dossier

| Dossier | Contenu |
|---------|---------|
| `data/` | Les fichiers CSV utilises dans les lecons |
| `exercices/` | Des exercices avec enonce et correction |

### Donnees disponibles

| Fichier | Description |
|---------|-------------|
| `consommation_energie.csv` | Consommation electricite et gaz par batiment et zone (~2 600 lignes) |
| `production_industrielle.csv` | Production par ligne et equipe, avec defauts (~1 500 lignes) |
| `capteurs_temperature.csv` | Releves de capteurs toutes les 15 minutes (~500 lignes) |

## Lecons sur le site

| # | Lecon | Duree |
|---|-------|-------|
| 1.1 | [Qu'est-ce que Claude Code ?](https://datamastery.dev/module-1/lecon-1-1-quest-ce-que-claude-code) | 30 min |
| 1.2 | [Installation](https://datamastery.dev/module-1/lecon-1-2-installation) | 45 min |
| 1.3 | [Premier graphique](https://datamastery.dev/module-1/lecon-1-3-premier-graphique) | 60 min |
| 1.4 | [Comprendre le dialogue](https://datamastery.dev/module-1/lecon-1-4-comprendre-le-dialogue) | 45 min |
| - | [Cas d'etude : energie](https://datamastery.dev/module-1/cas-etude-premier-graphique-energie) | 60 min |

## Besoin d'aide ?

- En cas de blocage, demander a Claude Code : "Reprends depuis le debut" ou "Qu'est-ce qui n'a pas marche ?"
- Pour les exercices, commencer par l'enonce puis comparer avec la correction
- La lecon 1.2 sur le site contient un guide de resolution des problemes courants
