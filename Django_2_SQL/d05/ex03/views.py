from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

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
    for movie in movies:
        try:
            m = Movies(episode_nb=movie[0], title=movie[1], director=movie[2], producer=movie[3], release_date=movie[4])
            m.save()
        except Exception as e:
            return HttpResponse(str(e))
    return HttpResponse("OK")

def display(request):
    try:
        data = Movies.objects.all()
        if not data:
            return HttpResponse("No data available")
        else:
            return render(request, 'ex03/display.html', {'movies': data})
    except Exception as e:
        return HttpResponse("No data available")