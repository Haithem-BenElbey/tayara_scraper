import os
from Item_IDs_scraper import get_tayara_ids
from Items_scraper import scrape_items
from transform_json2csv import json_to_csv

# Récupérer les variables d'environnement
category = os.environ.get("CATEGORY", "ImmoNeuf")
max_page = int(os.environ.get("MAX_PAGE", 5))
output_dir = os.environ.get("OUTPUT_DIR", "./data")

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

base_url = f"https://www.tayara.tn/ads/c/{category}/?page={{}}"

print(f"🔍 Catégorie : {category}")
print(f"📄 Nombre de pages à scraper : {max_page}")

# Étape 1 : Récupération des IDs
ids = get_tayara_ids(base_url, max_page=max_page)

# Étape 2 : Scraper les items et sauvegarder en JSON
json_file = os.path.join(output_dir, f"{category}_items.json")
scrape_items(ids, json_file)

# Étape 3 : Conversion JSON → CSV
csv_file = os.path.join(output_dir, f"{category}_items.csv")
json_to_csv(json_file, csv_file)

print(f"✅ Scraping terminé pour {category}")
print(f"📁 Fichiers générés : {json_file}, {csv_file}")
