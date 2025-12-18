import requests
import json
import os
import time

BASE_URL = "https://api.patentsview.org/patents/query"

def fetch_patents_by_year(year, page=1, per_page=1000):
    """
    Nouvelle version compatible PatentsView 2024.
    Recherche par année avec search_text.
    """

    params = {
        "q": f"patent_date:{year}",
        "f": json.dumps([
            "patent_number",
            "patent_title",
            "patent_date",
            "patent_application_date",
            "patent_abstract",
            "cpc_subgroup_id",
            "ipc_class",
            "assignee_organization",
            "assignee_country",
            "inventor_country",
            "patent_num_cited_by_us_patents"
        ]),
        "o": json.dumps({
            "page": page,
            "per_page": per_page
        })
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Erreur API : {response.status_code}")
        print("URL appelée :", response.url)
        return None

    return response.json()


def save_raw_data(year, page, data):
    """
    Sauvegarde JSON brute
    """
    os.makedirs("data/raw/uspto", exist_ok=True)
    filename = f"data/raw/uspto/uspto_{year}_page{page}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def run_etl_uspto(start_year=2010, end_year=2014, per_page=1000):
    for year in range(start_year, end_year + 1):
        print(f"=== Année {year} ===")
        page = 1

        while True:
            print(f" → Page {page}", end="")

            data = fetch_patents_by_year(year, page, per_page)

            # arrêt si vide
            if not data or "patents" not in data or len(data["patents"]) == 0:
                print(" (fin)")
                break

            save_raw_data(year, page, data)
            print(" ✓")

            page += 1
            time.sleep(0.3)

    print("=== ETL USPTO terminé ===")


if __name__ == "__main__":
    run_etl_uspto()

