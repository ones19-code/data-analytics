import pandas as pd
import os

PROCESSED = "data/processed/uspto/"
OUTFILE = PROCESSED + "uspto_master.parquet"



def load_csv(name):
    return pd.read_csv(PROCESSED + name, dtype=str, low_memory=False)



def make_cpc_main(df):
    if "cpc_group" not in df.columns:
        print(" Avertissement : colonne cpc_group absente.")
        return pd.DataFrame(columns=["patent_id", "cpc_main"])

    df = df.dropna(subset=["cpc_group"]).copy()
    df["cpc_main"] = df["cpc_group"].astype(str).str[:4]
    return df[["patent_id", "cpc_main"]].drop_duplicates()


def make_ipc_main(df):
    if "ipc_class" not in df.columns:
        print(" Avertissement : colonne ipc_class absente.")
        return pd.DataFrame(columns=["patent_id", "ipc_main"])

    df = df.dropna(subset=["ipc_class"]).copy()
    df["ipc_main"] = df["section"].astype(str) + df["ipc_class"].astype(str)
    return df[["patent_id", "ipc_main"]].drop_duplicates()


def make_assignee_country(df):
    if "assignee_country" not in df.columns:
        print(" Avertissement : colonne assignee_country absente.")
        return pd.DataFrame(columns=["patent_id", "assignee_country"])

    return df[["patent_id", "assignee_country"]].drop_duplicates()



def make_inventor_country(df):
    if "inventor_country" not in df.columns:
        print("Avertissement : colonne inventor_country absente.")
        return pd.DataFrame(columns=["patent_id", "inventor_country"])

    return df[["patent_id", "inventor_country"]].drop_duplicates()


def make_citation_count_chunked(filepath, chunksize=500000):
    print("→ Calcul des citations (chunked) ...")

    counts = {}

    for chunk in pd.read_csv(filepath, sep=",", dtype=str, chunksize=chunksize, low_memory=False):
        cited_list = chunk["citation_patent_id"].astype(str)

        for cited in cited_list:
            counts[cited] = counts.get(cited, 0) + 1

    print("→ Citations comptées.")

    df = pd.DataFrame(list(counts.items()), columns=["patent_id", "forward_citations"])
    return df


def run_merge():
    print("=== Fusion USPTO démarrée ===")

  
    patent = load_csv("patent_2010_2014.csv")
    abstract = load_csv("abstract_2010_2014.csv")
    cpc = load_csv("cpc_all.csv")
    ipc = load_csv("ipc_all.csv")
    assignee = load_csv("assignee_all.csv")
    inventor = load_csv("inventor_all.csv")

 
    citation_count = make_citation_count_chunked(PROCESSED + "citation_all.csv")


    cpc_main = make_cpc_main(cpc)
    ipc_main = make_ipc_main(ipc)
    assignee_clean = make_assignee_country(assignee)
    inventor_clean = make_inventor_country(inventor)

 
    df = patent.merge(abstract, on="patent_id", how="left")
    df = df.merge(cpc_main, on="patent_id", how="left")
    df = df.merge(ipc_main, on="patent_id", how="left")
    df = df.merge(assignee_clean, on="patent_id", how="left")
    df = df.merge(inventor_clean, on="patent_id", how="left")
    df = df.merge(citation_count, on="patent_id", how="left")

 
    df["year"] = pd.to_datetime(df["patent_date"], errors="coerce").dt.year


    df["forward_citations"] = df["forward_citations"].fillna(0).astype(int)


    df.to_parquet(OUTFILE, index=False)

    print("=== Fusion terminée ===")
    print(f"Fichier généré : {OUTFILE}")
    print(f"Nombre de lignes : {len(df):,}")


if __name__ == "__main__":
    run_merge()

