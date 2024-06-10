from django.db import models

class Planets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=128)
    diameter = models.IntegerField()
    orbital_period = models.IntegerField()
    population = models.BigIntegerField()
    rotation_period = models.IntegerField()
    surface_water = models.FloatField()
    terrain = models.CharField(max_length=128)

class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    hair_color = models.CharField(max_length=32)
    height = models.IntegerField()
    mass = models.FloatField()
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, to_field='name')