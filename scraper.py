import requests
from bs4 import BeautifulSoup
import json
import csv

# URL de l’annonce à scraper
url = "https://www.tayara.tn/item/685142a00e1c20e3eb0bf206"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 1️⃣ Récupérer le script JSON
script_tag = soup.find("script", id="__NEXT_DATA__", type="application/json")
if not script_tag:
    raise ValueError("❌ Script __NEXT_DATA__ introuvable")

data = json.loads(script_tag.string)

# 2️⃣ Naviguer dans la structure
ad_details = data["props"]["pageProps"]["adDetails"]
ad_params = ad_details.get("adParams", [])

# 3️⃣ Extraire les infos principales
ad_info = {
    "price": ad_details.get("price", ""),
    "delegation": ad_details.get("location", {}).get("delegation", ""),
    "governorate": ad_details.get("location", {}).get("governorate", ""),
    "category": ad_details.get("category", "")
}

# 4️⃣ Ajouter dynamiquement les champs de adParams (clé = label, valeur = value)
for param in ad_params:
    label = param.get("label", "").strip()
    value = param.get("value", "").strip()
    if label:
        ad_info[label] = value

# 5️⃣ Sauvegarder dans un CSV
with open("tayara_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=ad_info.keys())
    writer.writeheader()
    writer.writerow(ad_info)

print("✅ Données extraites :")
for k, v in ad_info.items():
    print(f"{k}: {v}")
