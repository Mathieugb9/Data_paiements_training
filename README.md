# Analyse de données de paiement — Python & SQL

Petit projet d'analyse de données de transactions bancaires, réalisé
en lien avec les enjeux du Cash Management (traitement et contrôle de
flux de paiement).

## Ce que fait le projet
- **Génération** d'un jeu de 2000 transactions fictives (`00_generer_donnees.py`)
- **Nettoyage & détection d'anomalies** (`01_analyse_donnees.ipynb`) :
  montants anormaux, dates incohérentes, devises invalides, montants
  nuls, doublons, et détection statistique par Z-score
- **Reporting** : analyse du volume par client et par mois (pandas)
- **Requêtes SQL** sur la base de transactions (`requetes.sql`)

## Technologies
Python (pandas, numpy), Jupyter, SQL (SQLite)

## Pistes d'amélioration
- Détection d'anomalies par Machine Learning (Isolation Forest ou autre algo unsupervised learning)
- Automatisation d'un reporting quotidien avec visualisations
- Connexion à une source de données en continu (SQL / API)
