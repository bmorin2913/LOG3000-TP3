# LOG3000 - TP3 

## Nom du projet 
* Calculatrice simple

## Numéro d’équipe
* Équipe 41

## Objectif

### But du projet

Le but de ce projet est de reprendre une application web de calculatrice simple développée en Python avec Flask et de transformer une base de code désorganisée et partiellement documentée en un projet structuré et documenté, prêt pour le travail collaboratif sur GitHub.

Ce travail met en avant les bonnes pratiques de gestion de versions, de documentation logicielle, de tests et de correction de bogues dans un contexte d’équipe.

### Portée du projet

La portée du projet inclut l’analyse et la documentation des composants existants (Frontend HTML/CSS et Backend Flask), la structuration du dépôt GitHub, l’ajout de documentation, la mise en place de tests, le suivi des problèmes via les issues, ainsi que la correction des bogues à l’aide d’un flux de branches et de pull requests.

Le projet vise la stabilisation de l’application existante, pas le développement de nouvelles fonctionnalités.

### Objectifs

#### Objectifs de réalisation

Dans le cadre du devoir, le travail consiste à :

- Ajouter la documentation manquante (docstrings, README de modules, commentaires utiles).
- Mettre en place un module de tests et documenter son utilisation.
- Identifier les bogues à l’aide de tests et ouvrir des issues associées.
- Corriger les bogues via des branches dédiées avec commits explicites.
- Valider les corrections par l’exécution complète des tests.

#### Objectifs de l'application

L'objectif de l'application de calculatrice web simple en elle-même est de permettre à l'utilisateur d'effectuer des additions, des soustractions, des multiplications et des divisions via une interface web intuitive.

## Prérequis d’installation
Pour exécuter ce projet localement, vous devez avoir :

* Python et pip installés.

## Guide d’installation

1. Accéder au dossier
```
cd LOG3000-TP3
```

2. Créer un environnement virtuel 
```
python -m venv venv
venv\Scripts\activate
```

3. Installer les dépendances 
```
pip install Flask
```

## Instructions d’utilisation détaillées 

Après avoir suivi toutes les étapes de l'installation, l'application est prête à être utilisée :

1. Lancer l'application :
```
python app.py 
```
2. Ouvrir l'application :

Accédez à l'application en cliquant sur le lien généré dans votre console ou en saisissant directement l'adresse http://localhost:5000 dans votre navigateur web.

3. Utilisation de la calculatrice :

* Saisir un premier chiffre à l'aide des boutons 0-9.
* Sélectionner une opération arithmétique (+, -, *, /).
* Saisir un deuxième chiffre à l'aide des boutons 0-9.
* Appuyer sur le bouton « = » pour obtenir le résultat du calcul.
* Appuyer sur le bouton « C » à tout moment pour réinitialiser la calculatrice.


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

## Flux de contribution
Afin d’assurer une collaboration efficace et de maintenir la qualité du code, le projet suit un flux de contribution structuré basé sur les bonnes pratiques Git et GitHub. Toute modification doit être liée à une issue, développée sur une branche dédiée et intégrée via une Pull Request révisée.

### 1. Branches
La stratégie de branches est la suivante :

- `main` : branche principale contenant la version stable du projet.
- `dev` : branche d’intégration pour le développement actif.
- `feature/<nom>` : ajout d’une fonctionnalité.
- `bugfix/<nom>` : correction d’un bogue.
- `hotfix/<nom>` : correctif urgent.

Règles :

- Une branche doit correspondre à une seule fonctionnalité ou un seul correctif.
- Chaque branche est créée à partir de `dev`.
- La branche doit rester synchronisée régulièrement avec `dev`.
- Les noms de branches doivent être courts, explicites et en minuscules avec tirets.


### 2. Messages de commit
Les messages doivent être concis et descriptifs.

Nous utilisons les préfixes suivants :

- `feat:` Nouvelle fonctionnalité.
- `fix:` Correction de bogue.
- `doc:` Modification de la documentation.
- `style:` Changements de formatage (espaces, virgules, etc.).
- `refactor:` Refactorisation du code sans changement de logique.
- `test:` Ajout ou modification de tests.
- `chore:` Tâches de maintenance ou mises à jour de dépendances.


*Exemple : `fix: corrige la division par zéro dans calculator.py`*

### 3. Pull Request
Toute modification doit être intégrée par Pull Request (PR).

Processus :

1. Créer une branche à partir de `dev`.
2. Implémenter la modification ou la correction.
3. Vérifier que les tests passent.
4. Ouvrir une Pull Request vers `dev`.
5. Lier la PR à l’issue correspondante.
6. Décrire clairement les changements effectués.
7. Demander une revue de code.
8. Fusionner seulement après validation.

Chaque Pull Request doit contenir :

- Une description claire
- La référence à l’issue associée
- La portée des changements

### 4. Issues
Tout bogue, problème ou amélioration doit être documenté dans une issue GitHub.

Chaque issue doit inclure :

- Un titre clair et précis
- Une description détaillée
- Une personne assignée
- Une étiquette appropriée (`bug`, `enhancement`, `test`, etc.)

Aucun correctif ne doit être effectué directement sur `main` ou `dev` sans issue et sans branche associée.

