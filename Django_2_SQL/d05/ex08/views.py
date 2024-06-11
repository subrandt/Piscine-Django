from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
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
                    homeworld INTEGER,
                    CONSTRAINT fk_homeworld FOREIGN KEY(homeworld) REFERENCES ex08_planets(id)
                );
            """)
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(str(e))

@csrf_exempt
def populate(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM ex08_people")
            cursor.execute("DELETE FROM ex08_planets")

            # First, populate the ex08_planets table
            with open('ex08/data/planets.csv', 'r') as f:
                reader = csv.reader(f, delimiter='\t')
                next(reader)  # Skip the header
                data = []
                for row in reader:
                    data.append([convert_to_null(value) for value in row])
                output = StringIO()
                writer = csv.writer(output, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(data)
                output.seek(0)
                cursor.copy_from(output, 'ex08_planets', sep='\t', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))

            # Print the data for debugging
            print(data)

            # Create a dictionary mapping planet names to their IDs
            cursor.execute("SELECT id, name FROM ex08_planets")
            planet_ids = {name: id for id, name in cursor.fetchall()}

            # Print the planet_ids to debug
            print(planet_ids)

            # Then, populate the ex08_people table
            with open('ex08/data/people.csv', 'r') as f:
                reader = csv.reader(f, delimiter='\t')
                next(reader)
                data = []
                for row in reader:
                    # Replace the homeworld name with its ID if it exists in planet_ids, otherwise skip the row
                    homeworld_id = planet_ids.get(row[-1])
                    if homeworld_id is not None:
                        row[-1] = homeworld_id
                        data.append([convert_to_null(value) for value in row])
                output = StringIO()
                writer = csv.writer(output, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(data)
                output.seek(0)
                cursor.copy_from(output, 'ex08_people', sep='\t', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))

            # Print the data for debugging
            # print(data)
            
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def display(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                SELECT people.name, planets.name, planets.climate
                FROM ex08_people AS people
                JOIN ex08_planets AS planets ON people.homeworld = planets.id
                WHERE planets.climate LIKE '%windy%' OR planets.climate LIKE '%moderately windy%'
                ORDER BY people.name ASC
            """)
            rows = cursor.fetchall()
            return render(request, 'ex08/display.html', {'rows': rows})
        except Exception as e:
            return HttpResponse("No data available")