import pandas as pd
import os

RAW = "data/raw/uspto/"
OUT = "data/processed/uspto/"
os.makedirs(OUT, exist_ok=True)

def filter_years_in_chunks(file_path, year_col, years, chunksize=200000):
    """
    Lit un gros TSV en morceaux (chunks) et ne conserve que les lignes
    dont la colonne year_col contient une année dans 'years'.
    """
    print(f"\n→ Filtrage {file_path} ...")

    filtered_chunks = []

    for chunk in pd.read_csv(
        file_path,
        sep="\t",
        dtype=str,
        chunksize=chunksize,
        low_memory=False,
    ):
        if year_col in chunk.columns:
            chunk[year_col] = pd.to_datetime(chunk[year_col], errors="coerce")
            filtered = chunk[chunk[year_col].dt.year.isin(years)]
        else:
            filtered = chunk  
        filtered_chunks.append(filtered)

    df = pd.concat(filtered_chunks, ignore_index=True)
    print("✓ Fait :", len(df), "lignes gardées")
    return df


def run_uspto_etl():
    years = {2010, 2011, 2012, 2013, 2014}

    print("=== ETL USPTO (g_*) DÉMARRÉ ===")

 
    patent = filter_years_in_chunks(
        RAW + "g_patent.tsv",
        year_col="patent_date",
        years=years,
    )

    
    abstract = filter_years_in_chunks(
        RAW + "g_patent_abstract.tsv",
        year_col="patent_date",
        years=years,
    )

    # CPC & IPC
    cpc = pd.read_csv(RAW + "g_cpc_current.tsv", sep="\t", dtype=str, low_memory=False)
    ipc = pd.read_csv(RAW + "g_ipc_at_issue.tsv", sep="\t", dtype=str, low_memory=False)

    # Assignees & Inventors 
    assignee = pd.read_csv(RAW + "g_assignee_disambiguated.tsv", sep="\t", dtype=str, low_memory=False)
    inventor = pd.read_csv(RAW + "g_inventor_disambiguated.tsv", sep="\t", dtype=str, low_memory=False)

    # Citations
    cite = pd.read_csv(RAW + "g_us_patent_citation.tsv", sep="\t", dtype=str, low_memory=False)

    patent.to_csv(OUT + "patent_2010_2014.csv", index=False)
    abstract.to_csv(OUT + "abstract_2010_2014.csv", index=False)
    cpc.to_csv(OUT + "cpc_all.csv", index=False)
    ipc.to_csv(OUT + "ipc_all.csv", index=False)
    assignee.to_csv(OUT + "assignee_all.csv", index=False)
    inventor.to_csv(OUT + "inventor_all.csv", index=False)
    cite.to_csv(OUT + "citation_all.csv", index=False)

    print("=== ETL USPTO TERMINÉ ===")


if __name__ == "__main__":
    run_uspto_etl()
