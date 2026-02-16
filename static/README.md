# Module `static`

## Raison d’être
Ce dossier contient les fichiers statiques utilisés par l’application web, notamment les styles CSS de l'application. Il permet de séparer la logique métier du style et des ressources statiques, facilitant ainsi la maintenance et l’évolution de l’interface utilisateur.

## Principaux fichiers et responsabilités
Ce dossier ne contient pas de logique métier, uniquement des ressources statiques nécessaires à l’affichage côté client.

- **style.css** : Feuille de style principale définissant l’apparence de l’interface utilisateur, notamment la mise en page, les couleurs, les boutons et l’affichage de la calculatrice.

## Dépendances ou hypothèses
- Il est supposé que le fichier CSS est lié dans les templates HTML du projet pour appliquer le style à l’application.
- Aucun framework CSS externe n’est utilisé, tout le style est défini localement.
