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



## ex02
http://127.0.0.1:8000/ex02/init/
http://127.0.0.1:8000/ex02/populate/
http://127.0.0.1:8000/ex02/display/



## ex03
faire les migrations de la DB avec:
    python3 manage.py makemigrations ex03
    python3 manage.py migrate
avant de tester

http://127.0.0.1:8000/ex03/populate/ - insere les données dans la DB
http://127.0.0.1:8000/ex03/display/ - affiche les données de la table movies


## ex04
http://127.0.0.1:8000/ex04/init/
http://127.0.0.1:8000/ex04/populate/
http://127.0.0.1:8000/ex04/display/
http://127.0.0.1:8000/ex04/remove/


## ex05
faire les migrations de la DB avec:
    python3 manage.py makemigrations ex05
    python3 manage.py migrate
avant de tester:

http://127.0.0.1:8000/ex05/populate/
http://127.0.0.1:8000/ex05/display/
http://127.0.0.1:8000/ex05/remove/


## ex06
http://127.0.0.1:8000/ex06/init/
http://127.0.0.1:8000/ex06/populate/
http://127.0.0.1:8000/ex06/display/
http://127.0.0.1:8000/ex06/remove/
http://127.0.0.1:8000/ex06/update/

## ex07
idem ex06 avec ORM
http://127.0.0.1:8000/ex07/populate/
http://127.0.0.1:8000/ex07/display/
http://127.0.0.1:8000/ex07/update/


## ex08
effacer la DB
psql -h localhost -U djangouser -d djangotraining
password secret
drop table ex08_planets cascade;
drop table ex08_people ;
\dt pour afficher les tables
\q pour quitter

http://127.0.0.1:8000/ex08/init/
http://127.0.0.1:8000/ex08/populate/
http://127.0.0.1:8000/ex08/display/

## ex09
python3 manage.py makemigrations ex09
python3 manage.py migrate

python3 manage.py loaddata ex09_initial_data.json
http://127.0.0.1:8000/ex09/display/


## ex10
python3 manage.py makemigrations ex10
python3 manage.py migrate

python manage.py loaddata ex10_initial_data.json
http://127.0.0.1:8000/ex10