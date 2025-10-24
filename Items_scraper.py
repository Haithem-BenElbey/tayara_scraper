# import json
# import requests
# from bs4 import BeautifulSoup
# from Item_IDs_scraper import get_tayara_ids  # importer ta fonction qui récupère les IDs

# def scrape_item(item_id):
#     """
#     Scrape une annonce Tayara par son ID et retourne un dictionnaire avec les infos.
#     """
#     url = f"https://www.tayara.tn/item/{item_id}"
#     headers = {"User-Agent": "Mozilla/5.0"}

#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print(f"Erreur lors du scraping de l'ID {item_id} : {response.status_code}")
#         return None

#     soup = BeautifulSoup(response.text, "html.parser")
#     script_tag = soup.find("script", id="__NEXT_DATA__", type="application/json")
#     if not script_tag:
#         print(f"❌ Script __NEXT_DATA__ introuvable pour l'ID {item_id}")
#         return None

#     data = json.loads(script_tag.string)
#     ad_details = data["props"]["pageProps"]["adDetails"]
#     ad_params = ad_details.get("adParams", [])

#     # Infos principales
#     ad_info = {
#         "price": ad_details.get("price", ""),
#         "delegation": ad_details.get("location", {}).get("delegation", ""),
#         "governorate": ad_details.get("location", {}).get("governorate", ""),
#         "category": ad_details.get("category", "")
#     }

#     # Ajouter dynamiquement les champs de adParams
#     for param in ad_params:
#         label = param.get("label", "").strip()
#         value = param.get("value", "").strip()
#         if label:
#             ad_info[label] = value

#     return ad_info

# def scrape_all_items(ids, output_file="tayara_items.json"):
#     """
#     Scrape tous les items à partir d'un ensemble d'IDs et sauvegarde dans un fichier JSON.
#     """
#     all_data = {}
#     for item_id in ids:
#         print(f"Scraping ID : {item_id}")
#         item_data = scrape_item(item_id)
#         if item_data:
#             all_data[item_id] = item_data

#     # Sauvegarder dans JSON
#     with open(output_file, "w", encoding="utf-8") as f:
#         json.dump(all_data, f, ensure_ascii=False, indent=4)

#     print(f"\n✅ Scraping terminé ! Données sauvegardées dans {output_file}")

# # Exemple d'utilisation
# if __name__ == "__main__":
#     base_url = "https://www.tayara.tn/ads/c/ImmoNeuf/?page={}"
#     ids = get_tayara_ids(base_url, max_page=10)  # récupère les IDs avec ton autre script
#     print(f"Total IDs récupérés : {len(ids)}")
#     scrape_all_items(ids)

import json
import requests
from bs4 import BeautifulSoup
import os

def scrape_items(item_ids, output_file="data/items.json"):
    """
    Scrape chaque item et enregistre les infos dans un JSON.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    all_data = {}
    for item_id in item_ids:
        url = f"https://www.tayara.tn/item/{item_id}"
        print(f"Scraping item {item_id}")
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", id="__NEXT_DATA__", type="application/json")
            if not script_tag:
                print(f"Script __NEXT_DATA__ introuvable pour item {item_id}")
                continue
            
            data = json.loads(script_tag.string)
            ad_details = data["props"]["pageProps"]["adDetails"]
            ad_params = ad_details.get("adParams", [])
            
            ad_info = {
                "price": ad_details.get("price", ""),
                "delegation": ad_details.get("location", {}).get("delegation", ""),
                "governorate": ad_details.get("location", {}).get("governorate", ""),
                "category": ad_details.get("category", "")
            }
            
            for param in ad_params:
                label = param.get("label", "").strip()
                value = param.get("value", "").strip()
                if label:
                    ad_info[label] = value
            
            all_data[item_id] = ad_info
            
        except Exception as e:
            print(f"Erreur scraping item {item_id}: {e}")
            continue
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSON sauvegardé : {output_file}")
