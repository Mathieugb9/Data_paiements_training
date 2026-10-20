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

-- pour lancer la requête dans le terminal, utilisez la commande suivante : apres avoir installer SQlite3 et avoir créé la base de données paiements.db, 
--vous pouvez exécuter le fichier requetes.sql en utilisant la commande suivante dans le terminal :
--sqlite3 paiements.db