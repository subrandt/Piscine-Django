from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from psycopg2 import sql, errors
import csv
from io import StringIO

def convert_to_null(value):
    return r"\N" if value == 'NULL' or value == '' else value

@csrf_exempt
def init(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    climate VARCHAR(128),
                    diameter INTEGER,
                    orbital_period INTEGER,
                    population BIGINT,
                    rotation_period INTEGER,
                    surface_water REAL,
                    terrain VARCHAR(128)
                );
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    birth_year VARCHAR(32),
                    gender VARCHAR(32),
                    eye_color VARCHAR(32),
                    hair_color VARCHAR(32),
                    height INTEGER,
                    mass REAL,
                    homeworld VARCHAR(64),
                    CONSTRAINT fk_homeworld FOREIGN KEY(homeworld) REFERENCES ex08_planets(name)
                );
            """)
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(str(e))

@csrf_exempt

def populate(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE ex08_planets, ex08_people RESTART IDENTITY CASCADE")
            with open('ex08/data/planets.csv', 'r') as f:
                cursor.copy_from(f, 'ex08_planets', sep='\t', null='NULL', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))
            with open('ex08/data/people.csv', 'r') as f:
                cursor.copy_from(f, 'ex08_people', sep='\t', null='NULL', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))
    except errors.UniqueViolation:
        return HttpResponse("Error: Unique key violation")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
    return HttpResponse("Planets OK<br>People OK")

def display(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                SELECT people.name, planets.name, planets.climate
                FROM ex08_people AS people
                JOIN ex08_planets AS planets ON people.homeworld = planets.name
                WHERE planets.climate LIKE '%windy%' OR planets.climate LIKE '%moderately windy%'
                ORDER BY people.name ASC
            """)
            rows = cursor.fetchall()
            return render(request, 'ex08/display.html', {'rows': rows})
        except Exception as e:
            return HttpResponse("No data available")

def debug(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM ex08_planets")
        planet_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM ex08_people")
        people_count = cursor.fetchone()[0]
    return HttpResponse(f"Planets: {planet_count}, People: {people_count}")