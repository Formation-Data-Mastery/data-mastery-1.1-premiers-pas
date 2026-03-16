# Projet Data Mastery — Module 1

## Environnement

- Python géré avec uv (pas pip)
- Pour installer un package : `uv add nom-du-package`
- Pour exécuter du code : `uv run python script.py`
- IMPORTANT : ne JAMAIS utiliser pip, python -m pip, ou .venv/bin/pip — toujours uv add

## Contexte

Ce projet est un module de formation pour débutants. Les données sont dans `data/`. Les résultats (graphiques, notebooks) vont dans `output/` ou `notebooks/`.

## Conventions

- Commentaires en français, simples et pédagogiques
- Un concept par cellule dans les notebooks Jupyter
- Toujours expliquer le "pourquoi" avant le "comment"

## Graphiques Plotly

Les graphiques doivent être soignés et professionnels :

- Utiliser un template propre : `template="plotly_white"` ou `template="seaborn"`
- Palette de couleurs harmonieuse (éviter les couleurs par défaut)
- Titres lisibles, taille suffisante (`title_font_size=18`)
- Axes avec noms explicites en français et unités
- Légende positionnée clairement (pas par-dessus les données)
- Marges ajustées : `fig.update_layout(margin=dict(l=60, r=30, t=60, b=60))`
- Taille adaptée : `width=800, height=500` minimum
- Toujours afficher dans le notebook (`fig.show()`) ET sauvegarder en HTML (`fig.write_html()`)
