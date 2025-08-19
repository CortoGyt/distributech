# Distributech ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MySQL](https://img.shields.io/badge/MySQL-8+-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

### Description
Pipeline ETL pour gérer les données de production et de commandes : extraction, transformation, chargement dans MySQL, et export du stock disponible.

---

### 📂 Structure du projet

```
data/
base_stock.sqlite
commande_revendeur_tech_express.csv
transform/ (CSV transformés et exportés)
scripts/
    extraire_donnees.py
    transformer_donnees.py
    create_db.py
    load_db.py
    procedure.py
    Main.py
bdd/db/docker-compose.yml (MySQL + Adminer)
.env (DB_USER et DB_PASSWORD)
```

---

### Installation

**Cloner le dépôt**
```bash
git clone <votre_repo_url>
cd project
```

**Installer les dépendances Python**
```bash
pip install pandas mysql-connector-python python-dotenv
```

**Créer un fichier .env avec vos identifiants MySQL**
```
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
```

---

### Docker (optionnel)

Pour lancer MySQL et Adminer via Docker Compose depuis bdd/db :
```bash
cd bdd/db
docker-compose up -d
```

- **MySQL** : localhost:3306 (root password: votreMotDePasse)
- **Adminer** : http://localhost:8080

Le dossier `./db` est dans `.gitignore` et contient les données persistantes MySQL.

---

### Usages

**Exécuter le pipeline complet :**
```bash
python scripts/Main.py
```

Étapes réalisées automatiquement :

- **Extraction** : SQLite + CSV → DataFrames
- **Transformation** : Nettoyage, calculs, génération CSV
- **Création MySQL** : Tables et relations
- **Chargement** : Procédure maj_stocks pour insérer les données
- **Export stock** : CSV stock_disponible.csv dans data/transform/

---

### Fichiers clés

- `extraire_donnees.py` : Extraction des données brutes
- `transformer_donnees.py` : Nettoyage et transformation
- `create_db.py` : Création des tables MySQL
- `load_db.py` : Chargement des données via procédure stockée
- `procedure.py` : Export CSV stock disponible
- `Main.py` : Orchestration complète du pipeline
- `docker-compose.yml` : MySQL + Adminer pour développement local

---

### Notes

- Assurez-vous que MySQL est accessible sur localhost:3306
- Les fichiers transformés et exports sont stockés dans `data/transform/`
- Les identifiants sont sécurisés via `.env`
- Docker est optionnel mais pratique pour lancer une base propre rapidement