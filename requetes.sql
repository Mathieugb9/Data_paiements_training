-- Importer le fichier CSV dans SQLite
.mode csv
DROP TABLE IF EXISTS transactions;
.import transactions.csv transactions

-- Afficher les 10 premières lignes
.headers on
.mode column
SELECT * FROM transactions LIMIT 10;

-- Compter le nombre de transactions
SELECT COUNT(*) AS nombre_transactions
FROM transactions;
-- les dix plus gros montants de transactions
SELECT date, client, montant, devise, pays
FROM transactions
ORDER BY montant DESC
LIMIT 10;

SELECT date,client , montant, devise, pays
FROM transactions
ORDER BY montant ASC
LIMIT 10;


#sqlite3 paiements.db