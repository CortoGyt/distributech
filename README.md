# Distributech ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MySQL](https://img.shields.io/badge/MySQL-8+-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Table des matières
1. [Description](#description)
2. [Fonctionnalités](#fonctionnalités)
3. [Prérequis](#prérequis)
4. [Technologies et langages](#technologies-et-langages)
5. [Installation](#installation)
6. [Guide de développement](#guide-de-développement)
7. [Licence](#licence)
8. [Créateurs](#créateurs)
9. [Liens utiles](#liens-utiles)

## Description
Pipeline ETL pour gérer les données de production et de commandes : extraction, transformation, chargement dans MySQL, et export du stock disponible.

## Fonctionnalités
- Extraction des données depuis SQLite et CSV
- Transformation et nettoyage des données
- Création et gestion de tables MySQL
- Chargement des données via procédure stockée
- Export du stock disponible en CSV
- Option Docker pour MySQL + Adminer

## Prérequis
- Python 3.10+
- MySQL 8+ (ou Docker pour MySQL)
- pip
- Docker (optionnel)

## Technologies et langages
- Python (pandas, mysql-connector-python, python-dotenv)
- MySQL
- Docker (optionnel)
- CSV/SQLite pour stockage temporaire

## Installation
### Cloner le dépôt
git clone https://github.com/CortoGyt/distributech.git \
cd distributech

### Installer les dépendances Python
pip install pandas mysql-connector-python python-dotenv

### Créer un fichier `.env`
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe


## Docker (optionnel)
Pour lancer MySQL et Adminer via Docker Compose depuis `bdd/db` :
cd bdd/db
docker-compose up -d

- MySQL : localhost:3306 (root password: votre_mot_de_passe)
- Adminer : http://localhost:8080
Le dossier `./db` est dans `.gitignore` et contient les données persistantes MySQL.

## Guide de développement
### Exécution du pipeline complet
python scripts/Main.py

### Étapes réalisées automatiquement
1. Extraction : SQLite + CSV → DataFrames
2. Transformation : Nettoyage, calculs, génération CSV
3. Création MySQL : Tables et relations
4. Chargement : Procédure `maj_stocks` pour insérer les données
5. Export stock : CSV `stock_disponible.csv` dans `data/transform/`

### Fichiers clés
- `extraire_donnees.py` : Extraction des données brutes
- `transformer_donnees.py` : Nettoyage et transformation
- `create_db.py` : Création des tables MySQL
- `load_db.py` : Chargement des données via procédure stockée
- `procedure.py` : Export CSV stock disponible
- `Main.py` : Orchestration complète du pipeline
- `docker-compose.yml` : MySQL + Adminer pour développement local

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Créateurs
- [Khaoula MILI](https://www.linkedin.com/in/hugo-babin-878451239/)
- [Hugo BABIN](https://www.linkedin.com/in/khaoula-mili/)
- [Corto GAYET](https://www.linkedin.com/in/corto-gayet-246aa32b3/)

## Liens utiles
- [GitHub](https://github.com/CortoGyt/distributech)
- [LinkedIn](https://www.linkedin.com/in/corto-gayet-246aa32b3/)
