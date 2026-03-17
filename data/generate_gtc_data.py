"""
Générateur de données GTC pour le cas d'étude.
Crée un fichier export_gtc_brut.csv avec ~2615 lignes de données réalistes.

Patterns réalistes :
- Consommation gaz inversement corrélée avec température (r ≈ -0.86)
- Consommation électricité NON corrélée avec température (r ≈ -0.05)
- Zone production domine la consommation
- Anomalies injectées : NaN, valeurs négatives, doublons, formats dates incorrects
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Configuration
np.random.seed(2025)
BATIMENTS = ['Usine Nord', 'Usine Sud']
ZONES = ['Production', 'Tertiaire', 'Logistique', 'Maintenance']
ENERGIE_TYPES = ['Gaz', 'Électricité']
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

def generer_temperature():
    """Température extérieure avec variations saisonnières réalistes."""
    n_jours = (END_DATE - START_DATE).days + 1
    jour_annee = np.arange(n_jours)

    # Tendance saisonnière (hiver froid, été chaud)
    # Décalage de 100 jours pour que le pic soit vers mi-juillet (jour ~190)
    tendance = 10 + 12 * np.sin(2 * np.pi * (jour_annee - 100) / 365)

    # Bruit aléatoire
    bruit = np.random.normal(0, 3, n_jours)

    return tendance + bruit

def generer_donnees():
    """Génère l'ensemble des données avant injection d'anomalies."""

    # Calendrier
    n_jours = (END_DATE - START_DATE).days + 1
    temperatures = generer_temperature()

    donnees = []

    for idx_jour in range(n_jours):
        date = START_DATE + timedelta(days=idx_jour)
        temp = temperatures[idx_jour]

        # Occupation varie par jour (moindre occupation le week-end)
        occupation = 60 + 30 * np.sin(2 * np.pi * idx_jour / 7) + np.random.normal(0, 5)
        occupation = np.clip(occupation, 20, 100)

        # Génération par bâtiment et zone
        for batiment in BATIMENTS:
            for zone in ZONES:
                # Sous-échantillonnage : les compteurs GTC ne transmettent pas tous les jours
                # 365 j × 2 bât × 4 zones × 2 énergies = 5840 ; × 0.45 ≈ 2628 lignes cible
                TAUX_PRESENCE = 0.45

                # Offset par zone : Production domine (>50%), les autres sont proches entre elles
                if zone == 'Production':
                    offset_zone = 80
                elif zone == 'Logistique':
                    offset_zone = 12
                elif zone == 'Tertiaire':
                    offset_zone = 10
                else:  # Maintenance
                    offset_zone = 8

                # Gaz : corrélation inverse forte avec température (r ≈ -0.85)
                # Pente élevée (5.0) pour que la température domine les offsets de zone
                if np.random.random() < TAUX_PRESENCE:
                    gaz = offset_zone + 5.0 * (25 - temp) + np.random.normal(0, 3)
                    gaz = max(0.5, gaz)
                    donnees.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'batiment': batiment,
                        'zone': zone,
                        'kwh': round(gaz, 2),
                        'temperature_ext': round(temp, 2),
                        'occupation_pct': round(occupation, 1),
                        'type_energie': 'gaz'
                    })

                # Électricité : pas de corrélation avec température
                # L'offset de zone pilote le niveau (Production consomme beaucoup plus)
                if np.random.random() < TAUX_PRESENCE:
                    electricite = offset_zone * 3.0 + np.random.normal(0, 10)
                    electricite = max(0.5, electricite)
                    donnees.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'batiment': batiment,
                        'zone': zone,
                        'kwh': round(electricite, 2),
                        'temperature_ext': round(temp, 2),
                        'occupation_pct': round(occupation, 1),
                        'type_energie': 'electricite'
                    })

    return pd.DataFrame(donnees)

def injecter_anomalies(df):
    """Injecte 22 anomalies réalistes dans le DataFrame."""

    df = df.copy()
    n_lignes = len(df)

    # 1. 12 valeurs NaN (capteurs hors ligne)
    indices_nan = np.random.choice(n_lignes, 12, replace=False)
    df.loc[indices_nan, 'kwh'] = np.nan

    # 2. 3 valeurs négatives (erreurs de compteur)
    indices_negatifs = np.random.choice(n_lignes, 3, replace=False)
    df.loc[indices_negatifs, 'kwh'] = -abs(df.loc[indices_negatifs, 'kwh'])

    # 3. 5 doublons (export GTC mal configuré)
    # Dupliquer 5 lignes aléatoires
    indices_doublons = np.random.choice(n_lignes, 5, replace=False)
    lignes_doublons = df.iloc[indices_doublons].copy()
    df = pd.concat([df, lignes_doublons], ignore_index=True)

    # 4. 2 dates mal formatées (DD/MM/YYYY au lieu de YYYY-MM-DD)
    indices_dates = np.random.choice(n_lignes, 2, replace=False)
    for idx in indices_dates:
        date_obj = datetime.strptime(df.loc[idx, 'date'], '%Y-%m-%d')
        df.loc[idx, 'date'] = date_obj.strftime('%d/%m/%Y')

    return df.reset_index(drop=True)

def main():
    """Crée et sauvegarde le fichier CSV."""

    print("Génération des données GTC...")
    df = generer_donnees()

    print(f"Nombre de lignes avant anomalies : {len(df)}")
    print(f"Nombre de colonnes : {len(df.columns)}")
    print(f"Colonnes : {list(df.columns)}")

    print("\nInjection des anomalies...")
    df = injecter_anomalies(df)

    print(f"Nombre de lignes après anomalies : {len(df)}")
    print(f"Anomalies injectées :")
    print(f"  - Valeurs NaN : {df['kwh'].isna().sum()}")
    print(f"  - Valeurs négatives : {(df['kwh'] < 0).sum()}")

    # Sauvegarde
    from pathlib import Path
    chemin_sortie = Path(__file__).parent / 'export_gtc_brut.csv'
    df.to_csv(chemin_sortie, index=False)

    print(f"\nFichier généré : {chemin_sortie}")
    print(f"Total de lignes : {len(df)}")
    print("\nAperçu des premières lignes :")
    print(df.head(10))

    # Vérifications
    print("\n--- Vérifications ---")
    print(f"Nombre de bâtiments : {df['batiment'].nunique()}")
    print(f"Nombre de zones : {df['zone'].nunique()}")
    print(f"Types d'énergie : {df['type_energie'].unique().tolist()}")
    print(f"Plage de dates : {df['date'].min()} à {df['date'].max()}")

if __name__ == '__main__':
    main()
