# Installation et configuration de PostgreSQL pour le projet Django

## Étape 1 : Installation de PostgreSQL

Ouvrez un terminal et exécutez la commande suivante pour installer PostgreSQL :

```bash
sudo apt-get install postgresql postgresql-contrib
```

## Étape 2 : Création de la base de données et de l'utilisateur

Exécutez les commandes suivantes pour créer une nouvelle base de données et un nouvel utilisateur :

```bash
sudo -u postgres psql
```

Une fois que vous êtes dans l'invite de commande de PostgreSQL, exécutez les commandes suivantes :

```bash
CREATE DATABASE djangotraining;
CREATE USER djangouser WITH PASSWORD 'secret';
GRANT ALL PRIVILEGES ON DATABASE djangotraining TO djangouser;
\q
```

## Étape 3 : Activation de l'environnement virtuel

Avant d'installer les dépendances du projet, vous devez activer votre environnement virtuel. Si vous avez déjà créé un environnement virtuel pour votre projet, vous pouvez l'activer en utilisant le script :

```
source create_virtualenv.sh
```

pour nettoyer l'environnement virtuel:
```
source clean_up.sh
```


## Étape 4 : Configuration du projet Django
Ouvrez le fichier settings.py de votre projet Django et modifiez la configuration de la base de données pour utiliser la nouvelle base de données et l'utilisateur que vous venez de créer :

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangotraining',
        'USER': 'djangouser',
        'PASSWORD': 'secret',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```