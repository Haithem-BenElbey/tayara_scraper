# import json
# import requests
# from bs4 import BeautifulSoup

# def get_tayara_ids(base_url, max_page=5):
#     """
#     Récupère tous les IDs des annonces Tayara pour les pages de 1 à max_page.
    
#     Args:
#         base_url (str): URL générale avec pagination, exemple: "https://www.tayara.tn/ads/c/ImmoNeuf/?page={}"
#         max_page (int): Nombre de pages à parcourir
    
#     Returns:
#         set: Ensemble des IDs uniques des annonces
#     """
#     all_ids = set()
    
#     for page in range(1, max_page + 1):
#         url = base_url.format(page)
#         print(f"Scraping page: {page} -> {url}")
        
#         try:
#             r = requests.get(url)
#             r.raise_for_status()
#         except Exception as e:
#             print(f"Erreur lors de la requête {url}: {e}")
#             continue
        
#         soup = BeautifulSoup(r.text, "html.parser")
#         script_tag = soup.find("script", id="__NEXT_DATA__")
#         if not script_tag:
#             print(f"Aucun script __NEXT_DATA__ trouvé sur la page {url}")
#             continue
        
#         try:
#             data = script_tag.string
#             json_data = json.loads(data)
            
#             # Chemins vers les annonces
#             new_hits = json_data["props"]["pageProps"]["searchedListingsAction"].get("newHits", [])
#             premium_hits = json_data["props"]["pageProps"]["searchedListingsAction"].get("premiumHits", [])
            
#             # Extraire les IDs
#             new_ids = [item["id"] for item in new_hits]
#             premium_ids = [item["id"] for item in premium_hits]
            
#             # Ajouter à l'ensemble
#             all_ids.update(new_ids)
#             all_ids.update(premium_ids)
            
#         except Exception as e:
#             print(f"Erreur lors du parsing JSON de la page {url}: {e}")
#             continue
    
#     return all_ids

# # Exemple d'utilisation
# if __name__ == "__main__":
#     base_url = "https://www.tayara.tn/ads/c/ImmoNeuf/?page={}"
#     ids = get_tayara_ids(base_url, max_page=50)
#     print(f"Nombre total d'IDs uniques trouvés: {len(ids)}")

import json
import requests
from bs4 import BeautifulSoup

def get_tayara_ids(base_url, max_page=5):
    """
    Récupère tous les IDs des annonces Tayara pour les pages de 1 à max_page.
    """
    all_ids = set()
    
    for page in range(1, max_page + 1):
        url = base_url.format(page)
        print(f"Scraping page: {page} -> {url}")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except Exception as e:
            print(f"Erreur lors de la requête {url}: {e}")
            continue
        
        soup = BeautifulSoup(r.text, "html.parser")
        script_tag = soup.find("script", id="__NEXT_DATA__")
        if not script_tag:
            print(f"Aucun script __NEXT_DATA__ trouvé sur la page {url}")
            continue
        
        try:
            data = json.loads(script_tag.string)
            new_hits = data["props"]["pageProps"]["searchedListingsAction"].get("newHits", [])
            premium_hits = data["props"]["pageProps"]["searchedListingsAction"].get("premiumHits", [])
            new_ids = [item["id"] for item in new_hits]
            premium_ids = [item["id"] for item in premium_hits]
            all_ids.update(new_ids)
            all_ids.update(premium_ids)
        except Exception as e:
            print(f"Erreur parsing JSON page {url}: {e}")
            continue
    
    return all_ids
