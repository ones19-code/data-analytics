# Data Dictionary — Dataset de brevets unifié

Chaque ligne correspond à **une publication de brevet** (niveau publication).

| Nom de colonne                 | Type      | Description courte                                           | Exemple                           | Commentaires |
|--------------------------------|-----------|--------------------------------------------------------------|-----------------------------------|--------------|
| doc_id                         | string    | Identifiant unique               | `US-20130012345-A1`               | ID interne unifié |
| source_list                    | string    | Liste des sources ayant fourni cette donnée                 | `USPTO;EPO;WIPO`                  | Séparateur `;` |
| pub_number                     | string    | Numéro de publication                                       | `20130012345`                     | |
| pub_kind                       | string    | Code de type de publication                                 | `A1`                              | |
| app_number                     | string    | Numéro de demande (si disponible)                           | `14/123456`                       | |
| family_id                      | string    | Identifiant de famille (DOCDB/WIPO)                         | `WO2012XXXXX`                     | |
| filing_date                    | date      | Date de dépôt                                               | `2011-07-20`                      | |
| pub_date                       | date      | Date de publication                                         | `2013-01-10`                      | |
| grant_date                     | date      | Date de délivrance (si disponible)                          | `2015-03-20`                      | |
| priority_date_first            | date      | Première date de priorité                                   | `2011-01-04`                      | |
| assignee_name_primary          | string    | Déposant / cessionnaire principal                           | `Siemens AG`                      | |
| assignee_country_primary       | string    | Pays du déposant (ISO2)                                     | `DE`                              | |
| inventor_count                 | int       | Nombre d’inventeurs                                         | `3`                               | |
| inventor_country_primary       | string    | Pays principal des inventeurs                               | `US`                              | |
| ipc_main                       | string    | Classe IPC principale                                       | `H04L 29/08`                      | |
| ipc_all                        | string    | Toutes les classes IPC                                      | `H04L 29/08;G06F 15/16`           | |
| cpc_main                       | string    | Classe CPC principale                                       | `H04L 12/58`                      | |
| cpc_all                        | string    | Toutes les classes CPC                                      | `H04L 12/58;H04W 4/02`            | |
| title_en                       | string    | Titre en anglais                                            | `Network management method`       | |
| abstract_en                    | string    | Résumé en anglais                                           | `The invention relates to...`     | |
| backward_citations_count       | int       | Citations faites par ce brevet                              | `12`                              | |
| forward_citations_3y           | int       | Citations reçues dans les 3 ans après publication           | `5`                               | |
| forward_citations_total        | int       | Citations totales reçues                                    | `17`                              | |
| grant_status                   | string    | Statut du brevet (si disponible)                            | `granted`                         | |
| legal_events_count             | int       | Nombre d’évènements légaux                                  | `4`                               | |
| etl_source_timestamp           | datetime  | Date d'extraction ETL                                       | `2025-01-12T16:45:00`             | |
| record_quality_score           | float     | Score interne de complétude (0–1)                           | `0.87`                            | |
