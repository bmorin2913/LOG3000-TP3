# Module `backend`

## Raison d’être
Ce dossier contient la logique métier de l’application, notamment les opérations de calcul. Il contient la logique du code Python (traitement, routes, calculs).

## Principaux fichiers et responsabilités
Ce dossier ne contient pas de ressources statiques ou de templates, uniquement la logique Python de l’application.
- **operators.py** : Contient les fonctions de base pour les opérations arithmétiques (addition, soustraction, multiplication, division).

## Dépendances ou hypothèses
- Nécessite Flask pour exécuter le serveur web.
- Les fonctions de calcul sont importées dans app.py.
- Les templates et fichiers statiques sont attendus dans les dossiers respectifs à la racine du projet.
