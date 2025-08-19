def load_db():
    import mysql.connector as mysql
    from dotenv import load_dotenv
    import os

# chargement .env avec les données sensibles
    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

#si pas de credentials valid, pas d'accès
    if not user or not password:
        print("Variables d’environnement manquantes.")
        return

    conn = mysql.connect(
        host='localhost',
        user=user,
        password=password,
        database='distributech',
        port=3306
    )
    cur = conn.cursor()

    procedure_sql = """
    CREATE PROCEDURE maj_stocks(
        IN id_production INT,
        IN quantite_produit INT,
        IN date_production DATE,
        IN id_produit INT,
        IN nom_produit VARCHAR(255),
        IN cout_unitaire DECIMAL(10,2),
        IN quantite_commande INT,
        IN prix_unitaire DECIMAL(10,2),
        IN total_prix_commande DECIMAL(10,2),
        IN id_commande INT,
        IN numero_commande INT,
        IN date_commande DATE,
        IN id_revendeur INT,
        IN nom_revendeur VARCHAR(255),
        IN id_region INT,
        IN nom_region VARCHAR(255),
        IN id_panier INT,
        IN total_prix_panier DECIMAL(10,2)
    )
    BEGIN
        INSERT INTO produits (id_produit, nom_produit, cout_unitaire)
        VALUES (id_produit, nom_produit, cout_unitaire)
        ON DUPLICATE KEY UPDATE nom_produit=VALUES(nom_produit), cout_unitaire=VALUES(cout_unitaire);

        INSERT INTO productions (id_production, quantite_produit, date_production, id_produit)
        VALUES (id_production, quantite_produit, date_production, id_produit);

        INSERT INTO commandes_produits (id_commande, id_produit, prix_unitaire, quantite_commande, total_prix_commande)
        VALUES (id_commande, id_produit, prix_unitaire, quantite_commande, total_prix_commande);

        INSERT INTO regions (id_region, nom_region)
        VALUES (id_region, nom_region)
        ON DUPLICATE KEY UPDATE nom_region=VALUES(nom_region);

        INSERT INTO revendeurs (id_revendeur, nom_revendeur, id_region)
        VALUES (id_revendeur, nom_revendeur, id_region)
        ON DUPLICATE KEY UPDATE nom_revendeur=VALUES(nom_revendeur), id_region=VALUES(id_region);

        INSERT INTO paniers (id_panier, total_prix_panier)
        VALUES (id_panier, total_prix_panier)
        ON DUPLICATE KEY UPDATE total_prix_panier=VALUES(total_prix_panier);

        INSERT INTO commandes (id_commande, id_region, id_revendeur, id_panier)
        VALUES (id_commande, id_region, id_revendeur, id_panier);
    END
    """

    try:
        cur.execute("DROP PROCEDURE IF EXISTS maj_stocks")
        cur.execute(procedure_sql)
        conn.commit()
        print("Procédure maj_stocks créée avec succès.")
    except mysql.Error as err:
        print("Erreur MySQL:", err)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
