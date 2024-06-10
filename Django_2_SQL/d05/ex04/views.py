from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def init(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                CREATE TABLE  IF NOT EXISTS ex04_movies (
                    episode_nb INT PRIMARY KEY,
                    title VARCHAR(64) NOT NULL,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                )
            """)
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

def populate(request):
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]
    with connection.cursor() as cursor:
        for movie in movies:
            try:
                cursor.execute("INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (episode_nb) DO NOTHING", movie)
            except Exception as e:
                return HttpResponse(e)
    return HttpResponse("OK")

def display(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM ex04_movies")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")
            else:
                return render(request, 'ex04/display.html', {'movies': rows})
        except Exception as e:
            return HttpResponse("No data available")

def remove(request):
    with connection.cursor() as cursor:
        if request.method == 'POST':
            movie_id = request.POST.get('movie')
            if movie_id:
                try:
                    cursor.execute("DELETE FROM ex04_movies WHERE episode_nb = %s", [movie_id])
                except Exception as e:
                    return HttpResponse(e)
        try:
            cursor.execute("SELECT * FROM ex04_movies")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")
        except Exception as e:
            return HttpResponse("No data available")
    return render(request, 'ex04/remove.html', {'movies': rows})