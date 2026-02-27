# Tests

Ce dossier contient des tests unitaires pour le projet.

## Exécution des tests

Pour exécuter tous les tests, utilisez la commande suivante à la racine du projet :

```
python -m unittest discover tests
```

Vous pouvez aussi exécuter un fichier de test spécifique :

```
python -m unittest tests/test_operators.py
python -m unittest tests/test_app.py
```

## Couverture des tests

- **test_operators.py** :
  - Teste toutes les fonctions du fichier `backend/operators.py` (add, subtract, multiply, divide).
  - Vérifie les résultats attendus et détecte les erreurs de logique (ex : multiplication incorrecte, division par zéro).

- **test_app.py** :
  - Teste la fonction `calculate` du fichier `app.py`.
  - Vérifie le calcul des expressions valides, la gestion des erreurs de format, des opérandes invalides, et la division par zéro.
  - Vérifie l'affichage des différents boutons de la calculatrice

Les tests sont conçus pour détecter les erreurs dans les fonctions mathématiques et la logique de calcul de l'application.
