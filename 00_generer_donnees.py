import pandas as pd
import numpy as np

np.random.seed(19)
n = 2000 #2000 valeurs


clients = ["ACME-FR","BTA-CORP","CITROEN","DASSAULT", "THALES", "BFI-LUX", "TER-DE"]
devises = ["EUR","USD","GBP","CHF","JPY","CAD","BTC"]
pays = ["FR","DE","IT","ES","UK","US","JP","CA"]
types_de_paiement = ["PRELEVEMENT","VIREMENT","PAIEMENT_CARTE","CHEQUE"]


#creation du dictionnaire de clients fictifs :

df = pd.DataFrame({
    "date": np.random.choice(
        pd.date_range(start="2020-01-01", end="2020-12-31"),
        size=n,
    ),
    "client": np.random.choice(clients, n),
    "montant": np.round(np.random.exponential(5000, n), 2),
    "devise": np.random.choice(devises, n),
    "pays": np.random.choice(pays, n),
    "types_de_paiement": np.random.choice(types_de_paiement, n),
})

# Créer 5 anomalies distinctes pour chaque type.
idx_anomalies = np.random.choice(df.index, size=20, replace=False)
idx_montants_eleves = idx_anomalies[:5]
idx_dates_incoherentes = idx_anomalies[5:10]
idx_devises_invalides = idx_anomalies[10:15]
idx_montants_nuls = idx_anomalies[15:]

df.loc[idx_montants_eleves, "montant"] = np.round(
    np.random.uniform(100000, 1000000, size=5), 2
)
df.loc[idx_dates_incoherentes, "date"] = np.random.choice(
    pd.date_range(start="2025-01-01", end="2025-12-31"), size=5
)
df.loc[idx_devises_invalides, "devise"] = np.random.choice(
    ["XYZ", "ABC", "DEF"], size=5
)
df.loc[idx_montants_nuls, "montant"] = 0

# Créer 5 duplicatas de facture avec des montants et des dates identiques.
idx_dup = np.random.choice(
    df.index.difference(idx_anomalies), size=5, replace=False
)
df = pd.concat([df, df.loc[idx_dup]], ignore_index=True)



df.to_csv("transactions.csv", index=False)
print("Fichier transactions.csv généré avec succès !")


