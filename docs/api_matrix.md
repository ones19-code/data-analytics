| USPTO (PatentsView API) | États-Unis (US patents) | ~1976–présent (nous utilisons 2010–2014) | API REST | JSON | Aucune authentification requise | Requêtes filtrées + pagination ; limite recommandée : 10 000 résultats/page max | Métadonnées (titre, dates, assignees, inventeurs), classifications IPC/CPC | Oui (backward & forward citations) | Titre + résumé (pas toujours le texte complet) | Statut légal partiel (pas complet ; pas idéal) | Mise à jour environ 1 fois/mois | Licence ouverte PatentsView ; usage analytique autorisé | Exemple : `https://api.patentsview.org/patents/query?q={"_gte":{"publication_date":"2010-01-01"}}&f=["patent_number","patent_title"]&page=1` |



| EPO OPS (Open Patent Services) | Europe (publications EP) | ~1978–présent (nous utilisons 2010–2014) | API REST | JSON | API-key gratuite obligatoire | Limite : ~60 requêtes/minute ; pagination obligatoire ; quota journalier limité | Métadonnées (titre, dates, priorités, demandeur, inventeurs), classifications IPC/CPC | Citations directes limitées (utiliser Google Patents pour compléter) | Titre + résumé (abstract) souvent disponibles | Pas de statut légal complet | Mise à jour fréquente, selon dépôts officiels | Usage analytique autorisé via l’API, pas de scraping | Exemple : `https://ops.epo.org/3.2/rest-services/published-data/publication/epodoc/EP1234567/biblio` |











| WIPO PATENTSCOPE | International (PCT / WO publications) | ~1978–présent (nous utilisons 2010–2014) | API REST | JSON | Aucune clé obligatoire (certaines limites sans clé) | Limite : env. 10 000 résultats/jour ; pagination nécessaire | Métadonnées (titre, dates, priorités, applicants, inventeurs), IPC/CPC | Citations non fournies directement (à compléter via sources tierces) | Résumé (abstract) souvent disponible ; texte complet parfois fourni | Pas de statut légal | Mise à jour régulière selon dépôts PCT | Usage analytique autorisé ; scraping interdit | Exemple : `https://patentscope.wipo.int/search/en/structuredSearch.jsf?publicationDateFrom=2010-01-01&publicationDateTo=2010-12-31&page=1` |
