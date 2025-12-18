import pandas as pd
import matplotlib.pyplot as plt

FILE = "data/processed/uspto/uspto_master.parquet"

def main():
    print("=== Load dataset ===")
    df = pd.read_parquet(FILE)
    print(df.head())
    print(df.info())
    print(df.describe(include='all'))

    # Count by year
    print("\n=== Patents per year ===")
    print(df['year'].value_counts().sort_index())

    df['year'].value_counts().sort_index().plot(kind='bar', figsize=(10,5))
    plt.title("Nombre de brevets par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre")
    plt.tight_layout()
    plt.show()


    df['forward_citations'].astype(int).hist(bins=50, figsize=(10,5))
    plt.title("Distribution des citations")
    plt.xlabel("Nombre de citations")
    plt.ylabel("Nombre de brevets")
    plt.show()


    print("\n=== CPC main top 10 ===")
    print(df['cpc_main'].value_counts().head(10))

if __name__ == "__main__":
    main()
