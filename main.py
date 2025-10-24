from Item_IDs_scraper import get_tayara_ids
from Items_scraper import scrape_items
from transform_json2csv import json_to_csv

def main():
    base_url = "https://www.tayara.tn/ads/c/ImmoNeuf/?page={}"
    print("1️⃣ Récupération des IDs")
    ids = get_tayara_ids(base_url, max_page=5)
    print(f"Total IDs récupérés : {len(ids)}")
    
    print("2️⃣ Scraping des items")
    scrape_items(ids, output_file="data/items.json")
    
    print("3️⃣ Transformation JSON -> CSV")
    json_to_csv(json_file="data/items.json", csv_file="data/items.csv")
    
    print("🎉 Terminé !")

if __name__ == "__main__":
    main()
