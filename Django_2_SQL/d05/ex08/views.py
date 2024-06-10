from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import csv
from io import StringIO

@csrf_exempt
def init(request):
   for filename in ['planets.csv', 'people.csv']:
    modified_filename = f'ex08/data/modified_{filename}'
    if not os.path.exists(modified_filename):
        with open(f'ex08/data/{filename}', 'r') as input_file, open(modified_filename, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # Write the header with the added id column
            header = next(reader)
            writer.writerow(['id'] + header)

            # Write the rows with the added id column
            for i, row in enumerate(reader, start=1):
                writer.writerow([i] + row)

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
                    homeworld VARCHAR(64)
                );
            """)
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

@csrf_exempt
def populate(request):
    with connection.cursor() as cursor:
        try:
            # Populate the planets table
            with open('ex08/data/planets.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header
                data = '\n'.join([','.join(row) for row in reader])
                f = StringIO(data)
                cursor.copy_from(f, 'ex08_planets', sep=',')
            # Populate the people table
            with open('ex08/data/people.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header
                data = '\n'.join([','.join(row) for row in reader])
                f = StringIO(data)
                cursor.copy_from(f, 'ex08_people', sep=',')
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

def display(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                SELECT people.name, planets.name, planets.climate
                FROM ex08_people AS people
                JOIN ex08_planets AS planets ON people.homeworld = planets.name
                WHERE planets.climate LIKE '%windy%'
                ORDER BY people.name ASC
            """)
            rows = cursor.fetchall()
            return render(request, 'ex08/display.html', {'rows': rows})
        except Exception as e:
            return HttpResponse("No data available")