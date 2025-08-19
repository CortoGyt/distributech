import mysql.connector as mysql
from dotenv import load_dotenv
import os


load_dotenv()
# credentials
conn = mysql.connect(
    host= 'localhost',
    user = os.getenv("DB_USER"),            
    password = os.getenv("DB_PASSWORD"),
    database = 'distributech',
    port=3306  
)

#cursor
cur = conn.cursor()

#drop si table déjà existante
cur.execute("DROP TABLE IF EXISTS commandes_produits")
cur.execute("DROP TABLE IF EXISTS productions")
cur.execute("DROP TABLE IF EXISTS commandes")
cur.execute("DROP TABLE IF EXISTS revendeurs")
cur.execute("DROP TABLE IF EXISTS produits")
cur.execute("DROP TABLE IF EXISTS regions")

# Création des tables
cur.execute("""
    CREATE TABLE regions (
    id_region INT PRIMARY KEY AUTO_INCREMENT,
    nom_region VARCHAR(255) NOT NULL
);
""")

cur.execute("""
    CREATE TABLE revendeurs (
    id_revendeur INT PRIMARY KEY AUTO_INCREMENT,
    nom_revendeur VARCHAR(255) NOT NULL,
    id_region INT NOT NULL,
    FOREIGN KEY (id_region) REFERENCES regions(id_region)
);
""")

cur.execute("""
CREATE TABLE produits (
    id_produit INT PRIMARY KEY AUTO_INCREMENT,
    nom_produit VARCHAR(255) NOT NULL,
    cout_unitaire DECIMAL(10,2) NOT NULL
);
""")

cur.execute("""
    CREATE TABLE productions (
    id_production INT PRIMARY KEY AUTO_INCREMENT,
    id_produit INT NOT NULL,
    quantite_production INT NOT NULL,
    date_production DATE NOT NULL,
    FOREIGN KEY (id_produit) REFERENCES produits(id_produit)
);
""")

cur.execute("""
    CREATE TABLE commandes (
    id_commande INT PRIMARY KEY AUTO_INCREMENT,
    numero_commande INT NOT NULL,
    date_commande DATE NOT NULL,
    total_panier INT NOT NULL,
    id_region INT NOT NULL,
    id_revendeur INT NOT NULL,
    FOREIGN KEY (id_region) REFERENCES regions(id_region),
    FOREIGN KEY (id_revendeur) REFERENCES revendeurs(id_revendeur)
);
""")

cur.execute("""
    CREATE TABLE commandes_produits (
    quantite_commande INT NOT NULL,
    total_commande INT NOT NULL,
    id_commande INT NOT NULL,
    id_produit INT NOT NULL,
    FOREIGN KEY (id_commande) REFERENCES commandes(id_commande),
    FOREIGN KEY (id_produit) REFERENCES produits(id_produit)
);
""")

# Insertion des regions
regions = [
    ("Île-de-France",),
    ("Occitanie",),
    ("Auvergne-Rhône-Alpes",),
    ("Bretagne",)
]
cur.executemany("INSERT INTO regions (nom_region) VALUES (%s);", regions)

# Insertion des revendeurs
revendeurs = [
    ("TechExpress", 1),
    ("ElectroZone", 1),
    ("SudTech", 2),
    ("GadgetShop", 2),
    ("Connectik", 3),
    ("Domotik+", 3),
    ("BreizhTech", 4),
    ("SmartBretagne", 4),
    ("HighNord", 1),
    ("OuestConnect", 4)
]
cur.executemany("INSERT INTO revendeurs (nom_revendeur, id_region) VALUES (%s,%s);", revendeurs)

# Insertion des produits
produits = [
    ("Casque Bluetooth", 59.90),
    ("Chargeur USB-C", 19.90),
    ("Enceinte Portable", 89.90),
    ("Batterie Externe", 24.90),
    ("Montre Connectée", 129.90),
    ("Webcam HD", 49.90),
    ("Hub USB 3.0", 34.90),
    ("Clavier sans fil", 44.90),
    ("Souris ergonomique", 39.90),
    ("Station d'accueil", 109.90)
]
cur.executemany("INSERT INTO produits (nom_produit, cout_unitaire) VALUES (%s,%s);", produits)

# Insertion de production (réapprovisionnement)
productions = [
    (1, 50, "2025-07-01"),
    (2, 80, "2025-07-01"),
    (3, 40, "2025-07-02"),
    (4, 60, "2025-07-02"),
    (5, 20, "2025-07-03"),
    (6, 35, "2025-07-03"),
    (7, 25, "2025-07-04"),
    (8, 30, "2025-07-04"),
    (9, 45, "2025-07-05"),
    (10, 15, "2025-07-05")
]
cur.executemany("INSERT INTO productions (id_produit, quantite_production, date_production) VALUES (%s,%s,%s);", productions)

#On commit et on ferme tout
conn.commit()
conn.close()

