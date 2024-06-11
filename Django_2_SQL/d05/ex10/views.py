from django.shortcuts import render
from .models import Movies, People, Planets

def search(request):
    if request.method == 'POST':
        min_date = request.POST.get('min_date')
        max_date = request.POST.get('max_date')
        diameter = request.POST.get('diameter')
        gender = request.POST.get('gender')

        results = People.objects.filter(
            gender=gender,
            movies__release_date__range=[min_date, max_date],
            homeworld__diameter__gte=diameter
        ).distinct()

        return render(request, 'results.html', {'results': results})

    genders = People.objects.values_list('gender', flat=True).distinct()
    return render(request, 'search.html', {'genders': genders})