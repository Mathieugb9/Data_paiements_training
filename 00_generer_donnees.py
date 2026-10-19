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
    "type_de_paiement": np.random.choice(types_de_paiement, n),
    "devise": np.random.choice(devises, n),
    "pays": np.random.choice(pays, n),
    "types_de_paiement": np.random.choice(types_de_paiement, n),
})

#Creer 15 anomalies dans le dataframe avec des montants elévés , des dates incohérantes , des devise non existantes , prix nuls 
idx = np.random.choice(df.index, size=15, replace=False)
df.loc[idx, "montant"] = np.round(np.random.uniform(100000, 1000000, size=15), 2)
df.loc[idx, "date"] = np.random.choice(pd.date_range(start="2025-01-01", end="2025-12-31"), size=15)
df.loc[idx, "devise"] = np.random.choice(["XYZ", "ABC", "DEF"], size=15)
df.loc[idx, "montant"] = 0

df.to_csv("transactions.csv", index=False)
print("Fichier transactions.csv généré avec succès !")


