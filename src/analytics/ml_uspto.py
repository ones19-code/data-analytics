import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from scipy.sparse import hstack

FILE = "data/processed/uspto/uspto_master.parquet"

def main():
    print("=== Load dataset ===")
    df = pd.read_parquet(FILE)

  
    df = df.sample(50000, random_state=42)

    df["high_impact"] = (df["forward_citations"] >= 10).astype(int)

    df["text"] = df["patent_title"].fillna("") + " " + df["patent_abstract"].fillna("")
    df["cpc"] = df["cpc_main"].fillna("NONE")


    vectorizer = TfidfVectorizer(max_features=2000)
    X_text = vectorizer.fit_transform(df["text"])

  
    X_year = df["year"].fillna(0).values.reshape(-1,1)

   
    X_cpc = pd.get_dummies(df["cpc"], sparse=True)


    X = hstack([X_text, X_year, X_cpc])

    y = df["high_impact"]

    print("→ Split train/test")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("→ Train RandomForest (fast mode)")
    model = RandomForestClassifier(n_estimators=150, n_jobs=-1)
    model.fit(X_train, y_train)

    print("=== Results ===")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
