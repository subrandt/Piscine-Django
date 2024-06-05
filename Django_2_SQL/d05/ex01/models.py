from django.db import models

# Un modèle Django est défini dans un fichier Python dans lequel une classe représente une table de base de données.
# Chaque attribut de la classe représente un champ de la table de base de données.
# Django ORM générera le SQL nécessaire pour créer cette table dans la base de données.

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
        return self.title
