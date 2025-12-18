import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
import xgboost as xgb

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

 
    X_year = df["year"].fillna(0).values.reshape(-1, 1)

 
    X_cpc = pd.get_dummies(df["cpc"], sparse=True)

  
    X = hstack([X_text, X_year, X_cpc])
    y = df["high_impact"]

    
    print("→ Split")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    train_d = xgb.DMatrix(X_train, label=y_train)
    test_d = xgb.DMatrix(X_test, label=y_test)

    # huny shn aaml modele 
    print("→ Training XGBoost...")
    params = {
        "max_depth": 6,
        "eta": 0.15,
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "scale_pos_weight": 3  
    }

    model = xgb.train(params, train_d, num_boost_round=200)

    print("→ Predict")
    preds = (model.predict(test_d) >= 0.5).astype(int)

    print("=== RESULTS (XGBoost) ===")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    main()
