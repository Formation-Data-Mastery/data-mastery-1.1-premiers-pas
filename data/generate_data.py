"""
generate_data.py
----------------
Génère trois jeux de données réalistes pour le Module 1 de la formation Data Mastery.

Exécution :
    python3 generate_data.py

Fichiers produits :
    consommation_energie.csv     (~2600 lignes)
    production_industrielle.csv  (~1500 lignes)
    capteurs_temperature.csv     (~500 lignes)
"""

import numpy as np
import pandas as pd
from pathlib import Path

# Graine aléatoire pour la reproductibilité
# "seed" fixe les valeurs aléatoires : relancer le script donnera toujours
# les mêmes données, ce qui est indispensable pour une formation.
RNG = np.random.default_rng(seed=42)

# Dossier de sortie = dossier contenant ce script
OUTPUT_DIR = Path(__file__).parent


# ---------------------------------------------------------------------------
# 1. CONSOMMATION ÉNERGIE — données GTC industriel
# ---------------------------------------------------------------------------

def generate_consommation_energie() -> pd.DataFrame:
    """
    Simule la consommation énergétique quotidienne d'un site industriel
    sur deux années (2023-2024).

    Chaque ligne = un relevé de compteur pour un bâtiment, une zone et un
    type d'énergie donnés. On couvre 4 bâtiments × ~1,5 relevé/jour en
    moyenne, ce qui produit ~2 600 lignes sur 730 jours.

    Patterns réalistes inclus :
    - Saisonnalité : plus de gaz en hiver, plus de climatisation en été
    - Anomalies : NaN, valeurs négatives, doublons, outliers
    """

    # Matrice de compteurs fixes par bâtiment :
    # chaque bâtiment dispose de quelques compteurs (zone + type_energie).
    # C'est réaliste : une usine n'a pas forcément tous les types de mesure.
    compteurs = [
        # (batiment,          zone,           type_energie)
        ("Usine_A",        "Production",    "electricite"),
        ("Usine_A",        "Production",    "gaz"),
        ("Usine_A",        "Eclairage",     "electricite"),
        ("Usine_B",        "Production",    "electricite"),
        ("Usine_B",        "Production",    "gaz"),
        ("Usine_B",        "Climatisation", "electricite"),
        ("Bureau_Central", "Bureaux",       "electricite"),
        ("Bureau_Central", "Climatisation", "electricite"),
        ("Bureau_Central", "Bureaux",       "gaz"),
        ("Entrepot_Nord",  "Production",    "electricite"),
        ("Entrepot_Nord",  "Eclairage",     "electricite"),
        ("Entrepot_Nord",  "Production",    "gaz"),
    ]
    # 12 compteurs × 730 jours = 8 760 avant doublons/NaN → trop.
    # On sous-échantillonne : chaque compteur n'envoie pas forcément chaque jour
    # (réseau GTC avec pertes de paquets ~70 % de présence).
    TAUX_PRESENCE = 0.30   # 30 % des jours × 12 compteurs × 730 j ≈ 2 628 lignes

    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")

    rows = []
    for date in dates:
        day_of_year = date.day_of_year
        # Courbe d'hiver : maximum autour du jour 15 (mi-janvier)
        winter_coef = 0.5 + 0.5 * np.cos(2 * np.pi * (day_of_year - 15) / 365)
        # Courbe d'été : maximum autour du jour 196 (mi-juillet)
        summer_coef = 0.5 + 0.5 * np.cos(2 * np.pi * (day_of_year - 196) / 365)

        for batiment, zone, type_energie in compteurs:
            # Sous-échantillonnage : simule les pertes de transmission GTC
            if RNG.random() > TAUX_PRESENCE:
                continue

            if type_energie == "gaz":
                # Le gaz chauffe : consommation dominée par l'hiver
                base = RNG.uniform(300, 1200)
                kwh = base * (0.4 + 0.6 * winter_coef)
            else:
                base = RNG.uniform(100, 800)
                if zone == "Production":
                    # La production tourne à plein toute l'année
                    kwh = base * RNG.uniform(0.85, 1.15)
                elif zone == "Climatisation":
                    # La clim consomme surtout en été
                    kwh = base * (0.2 + 0.8 * summer_coef)
                else:
                    kwh = base * RNG.uniform(0.8, 1.2)

            # Bruit aléatoire ±10 %
            kwh *= RNG.uniform(0.9, 1.1)
            kwh = round(kwh, 2)

            rows.append({
                "date": date.date(),
                "batiment": batiment,
                "zone": zone,
                "type_energie": type_energie,
                "kwh": kwh,
            })

    df = pd.DataFrame(rows)

    # --- Injection d'anomalies réalistes ---

    # 20 valeurs NaN : simule des capteurs hors ligne
    nan_idx = RNG.choice(df.index, size=20, replace=False)
    df.loc[nan_idx, "kwh"] = np.nan

    # 10 valeurs négatives : bug de compteur ou inversion de signe
    neg_idx = RNG.choice(df[df["kwh"].notna()].index, size=10, replace=False)
    df.loc[neg_idx, "kwh"] = -df.loc[neg_idx, "kwh"]

    # ~15 doublons : lignes envoyées deux fois par le système GTC
    dup_idx = RNG.choice(df.index, size=15, replace=False)
    duplicates = df.loc[dup_idx].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # 8 outliers extrêmes : pointe de consommation anormale (fuite, bug)
    outlier_idx = RNG.choice(df[df["kwh"].notna() & (df["kwh"] > 0)].index,
                             size=8, replace=False)
    df.loc[outlier_idx, "kwh"] = df.loc[outlier_idx, "kwh"] * RNG.uniform(5, 10,
                                                                           size=8)

    # Mélange aléatoire des lignes (les GTC n'envoient pas toujours dans l'ordre)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return df


# ---------------------------------------------------------------------------
# 2. PRODUCTION INDUSTRIELLE — suivi de ligne de fabrication
# ---------------------------------------------------------------------------

def generate_production_industrielle() -> pd.DataFrame:
    """
    Simule le suivi quotidien de trois lignes de production sur l'année 2024.

    Corrélations réalistes :
    - Les défauts augmentent avec le volume produit
    - Les arrêts sont plus fréquents sur certaines équipes
    """

    lignes = ["Ligne_1", "Ligne_2", "Ligne_3"]
    produits = ["Produit_A", "Produit_B", "Produit_C"]
    operateurs = ["Equipe_Matin", "Equipe_Apres_Midi", "Equipe_Nuit"]

    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")

    rows = []
    for date in dates:
        # Pas de production le dimanche (jour 6)
        if date.dayofweek == 6:
            continue

        for ligne in lignes:
            for produit in produits:
                # On n'a pas forcément tous les produits sur toutes les lignes
                # chaque jour — on tire aléatoirement une affectation.
                # Taux de présence ~53 % → 3×3×313 jours ouvrés×0.53 ≈ 1 500 lignes.
                if RNG.random() > 0.53:
                    continue  # cette combinaison n'est pas planifiée ce jour

                operateur = RNG.choice(operateurs)
                quantite_produite = int(RNG.integers(50, 501))

                # Les défauts sont proportionnels à la quantité (taux ~3 %)
                # avec une variance supplémentaire liée à l'équipe de nuit
                taux_defaut = 0.03
                if operateur == "Equipe_Nuit":
                    taux_defaut = 0.05  # fatigue → plus de défauts

                quantite_defauts = int(
                    RNG.binomial(n=quantite_produite, p=taux_defaut)
                )
                # Plafond à 25 pour rester réaliste
                quantite_defauts = min(quantite_defauts, 25)

                # Temps d'arrêt : souvent zéro, parfois significatif
                # np.random.exponential simule un phénomène rare mais coûteux
                temps_arret = int(min(RNG.exponential(scale=15), 120))

                rows.append({
                    "date": date.date(),
                    "ligne": ligne,
                    "produit": produit,
                    "quantite_produite": quantite_produite,
                    "quantite_defauts": quantite_defauts,
                    "temps_arret_min": temps_arret,
                    "operateur": operateur,
                })

    df = pd.DataFrame(rows)

    # --- Anomalies ---

    # NaN dans temps_arret_min : opérateur n'a pas rempli la fiche
    nan_arret_idx = RNG.choice(df.index, size=40, replace=False)
    df.loc[nan_arret_idx, "temps_arret_min"] = np.nan

    # Quelques défauts négatifs : erreur de saisie (soustraction au lieu d'addition)
    neg_def_idx = RNG.choice(df.index, size=6, replace=False)
    df.loc[neg_def_idx, "quantite_defauts"] = -abs(
        df.loc[neg_def_idx, "quantite_defauts"]
    )

    df = df.reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# 3. CAPTEURS TEMPÉRATURE — données IoT toutes les 15 minutes
# ---------------------------------------------------------------------------

def generate_capteurs_temperature() -> pd.DataFrame:
    """
    Simule cinq capteurs IoT sur 5 jours avec une mesure toutes les 15 minutes.

    Comportements spécifiques :
    - T03 : dérive progressive (capteur défaillant)
    - T05 : lacunes de lecture (perte de signal)
    """

    capteurs = ["T01", "T02", "T03", "T04", "T05"]
    # Une journée complète : 96 mesures × 15 min = 24 h
    # 96 timestamps × 4 capteurs fiables + 96 × 0.70 (T05) ≈ 451 lignes ≈ 500 cible
    timestamps = pd.date_range(
        start="2024-03-01 00:00:00",
        end="2024-03-01 23:45:00",
        freq="15min",
    )

    rows = []
    for step_idx, ts in enumerate(timestamps):
        # Cycle circadien : température plus basse la nuit, plus haute l'après-midi
        # Heure normalisée sur [0, 1] pour alimenter un sinus
        hour_fraction = (ts.hour + ts.minute / 60) / 24
        # Pic vers 14h (hour_fraction ≈ 0.58)
        daily_cycle = np.sin(2 * np.pi * (hour_fraction - 0.25))

        for capteur in capteurs:

            # T05 a des lacunes : environ 30 % des lectures manquent
            # (simule une perte de signal Wi-Fi)
            if capteur == "T05" and RNG.random() < 0.30:
                continue

            # Température de base 18-28°C modulée par le cycle journalier
            temp_base = 23 + 5 * daily_cycle

            if capteur == "T03":
                # Dérive progressive : +0.05°C par mesure (toutes les 15 min)
                # Sur 96 mesures = dérive totale de +4.8°C → clairement anormale
                drift = 0.05 * step_idx
                temp = temp_base + drift + RNG.normal(0, 0.3)
            else:
                temp = temp_base + RNG.normal(0, 0.5)

            # Humidité : corrélée inversement à la température (air chaud = moins humide)
            humidite = 50 - 0.8 * (temp - 23) + RNG.normal(0, 3)
            humidite = float(np.clip(humidite, 30, 70))

            rows.append({
                "timestamp": ts,
                "capteur_id": capteur,
                "temperature_c": round(float(temp), 2),
                "humidite_pct": round(humidite, 1),
            })

    df = pd.DataFrame(rows)
    return df


# ---------------------------------------------------------------------------
# POINT D'ENTRÉE
# ---------------------------------------------------------------------------

def main():
    print("Génération des données — Module 1 Data Mastery")
    print("=" * 50)

    # Dataset 1
    print("1/3  consommation_energie.csv ...")
    df_energie = generate_consommation_energie()
    path_energie = OUTPUT_DIR / "consommation_energie.csv"
    df_energie.to_csv(path_energie, index=False)
    print(f"     {len(df_energie):,} lignes  →  {path_energie}")

    # Dataset 2
    print("2/3  production_industrielle.csv ...")
    df_prod = generate_production_industrielle()
    path_prod = OUTPUT_DIR / "production_industrielle.csv"
    df_prod.to_csv(path_prod, index=False)
    print(f"     {len(df_prod):,} lignes  →  {path_prod}")

    # Dataset 3
    print("3/3  capteurs_temperature.csv ...")
    df_temp = generate_capteurs_temperature()
    path_temp = OUTPUT_DIR / "capteurs_temperature.csv"
    df_temp.to_csv(path_temp, index=False)
    print(f"     {len(df_temp):,} lignes  →  {path_temp}")

    print()
    print("Terminé. Résumé des fichiers générés :")
    print(f"  consommation_energie     : {len(df_energie):>6,} lignes")
    print(f"  production_industrielle  : {len(df_prod):>6,} lignes")
    print(f"  capteurs_temperature     : {len(df_temp):>6,} lignes")


if __name__ == "__main__":
    main()
