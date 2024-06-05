## ex00

lancer le serveur


http://127.0.0.1:8000/ex00/init
affiche OK

puis ouvrir un terminal, se connecter à la DB:
psql -h localhost -U djangouser -d djangotraining
mdp: secret

lister toutes les tables:
\dt
afficher la structure de la table:
\d ex00_movies

    Le nom de la table est ex00_movies.
    Les champs sont les suivants :
        title : chaîne de caractères variable, taille maximale de 64 octets, non null. Il est également unique, comme requis.
        episode_nb : entier, non null. C'est la clé primaire, comme requis.
        opening_crawl : texte, peut être null, sans limite de taille.
        director : chaîne de caractères variable, non null, taille maximale de 32 octets.
        producer : chaîne de caractères variable, non null, taille maximale de 128 octets.
        release_date : date (sans heure), non null.


## ex01
models.py crée la table dans la DB
Django ORM génère le SQL nécessaire
créer une migration pour le modèle Movies l'appliquer à la DB 
Une migration est un ensemble de commandes pour modifier la DB (par exemple, créer une nouvelle table, ajouter un champ à une table existante, etc.). Django ORM génère ces migrations en fonction des modifications apportés aux modèles.
puis executer dans le terminal:
    python3 manage.py makemigrations ex01
    python3 manage.py migrate

pour verifier la creation : tests unitaires
executer les tests avec:
    python3 manage.py test ex01

## ex02


## ex03
