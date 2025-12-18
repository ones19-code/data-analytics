# Patent API Benchmark & Unified ETL

Projet visant à comparer plusieurs sources de données de brevets (USPTO, EPO, WIPO, Google Patents)
et construire un dataset unifié pour l’analyse (classification, clustering, séries temporelles, géographie).

## Structure

- `data/raw/` : données brutes (API / dumps)
- `data/processed/` : données unifiées
- `docs/` : matrice API + data dictionary
- `notebooks/` : notebooks Jupyter
- `src/` : scripts ETL et analytics
- `run_logs/` : logs des appels API
- `report/` : rapport final
