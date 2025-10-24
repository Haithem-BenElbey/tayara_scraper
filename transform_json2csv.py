# import json
# import csv

# def collect_attributes(json_file):
#     """
#     Parcourt le JSON et retourne la liste de tous les attributs uniques.
#     """
#     with open(json_file, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     attributes = set()
#     for item_id, item_info in data.items():
#         attributes.update(item_info.keys())

#     return list(attributes)


# def json_to_csv(json_file, csv_file):
#     """
#     Transforme le JSON en CSV avec gestion des colonnes dynamiques.
#     Les valeurs manquantes sont remplacées par None.
#     """
#     with open(json_file, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     # Étape 1 : collecter toutes les colonnes uniques
#     columns = collect_attributes(json_file)

#     # Étape 2 : écrire le CSV
#     with open(csv_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=["id"] + columns)
#         writer.writeheader()
#         for item_id, item_info in data.items():
#             row = {"id": item_id}
#             for col in columns:
#                 row[col] = item_info.get(col, None)  # valeur None si manquante
#             writer.writerow(row)

#     print(f"✅ CSV créé : {csv_file}")


# # Exemple d'utilisation
# if __name__ == "__main__":
#     json_file = "tayara_items.json"
#     csv_file = "tayara_items.csv"
#     json_to_csv(json_file, csv_file)

import json
import csv
import os

def json_to_csv(json_file="data/items.json", csv_file="data/items.csv"):
    """
    Transforme un JSON en CSV en gérant les colonnes dynamiques.
    """
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Collecter toutes les clés uniques
    all_keys = set()
    for item in data.values():
        all_keys.update(item.keys())
    
    columns = ["id"] + sorted(all_keys)
    
    # Écrire CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for item_id, item_data in data.items():
            row = {"id": item_id}
            for key in all_keys:
                row[key] = item_data.get(key, None)
            writer.writerow(row)
    
    print(f"✅ CSV généré : {csv_file}")
