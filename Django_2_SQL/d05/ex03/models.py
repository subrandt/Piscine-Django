from django.db import models

class Movies(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, null=False)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    def __str__(self):
        return self.title