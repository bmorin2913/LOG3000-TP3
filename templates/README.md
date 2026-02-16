# Module `templates`

## Raison d’être
Ce dossier contient les fichiers de templates HTML utilisés par l’application web Flask. Il est responsable de la présentation et de l'affichage des interfaces utilisateurs.

## Principaux fichiers et responsabilités
Ce dossier ne contient pas de logique métier, uniquement des fichiers de présentation pour l’interface utilisateur.

- **index.html** : Template principal de l’interface de la calculatrice. Il définit la structure de la page, les boutons, l’affichage des résultats et inclut le style CSS. Il utilise la syntaxe Jinja2 pour afficher dynamiquement les résultats et intégrer les ressources statiques.

## Dépendances ou hypothèses
- Les templates sont rendus par Flask via la fonction `render_template`.
- Les fichiers HTML utilisent la syntaxe Jinja2 pour intégrer des variables et des liens vers les fichiers statiques.
- Il est supposé que le style CSS est correctement lié via `url_for('static', filename='style.css')`.
