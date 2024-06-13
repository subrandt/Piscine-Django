from django.shortcuts import render
from .models import Movies, People, Planets
from datetime import datetime

def search(request):
    results = []
    if request.method == 'POST':
        min_date = request.POST.get('min_date')
        max_date = request.POST.get('max_date')
        diameter = request.POST.get('diameter')
        gender = request.POST.get('gender')

        if not min_date:
            min_date = '1900-01-01'
        if not max_date:
            max_date = datetime.now().strftime('%Y-%m-%d')

        if diameter:
            diameter = int(diameter)
        else:
            diameter = 0

        results = People.objects.filter(
            gender=gender,
            movies__release_date__range=[min_date, max_date],
            homeworld__diameter__gte=diameter
        ).select_related('homeworld').prefetch_related('movies').distinct()

         # Store the IDs of the results in the session
        request.session['result_ids'] = list(results.values_list('id', flat=True))

    # Get the IDs from the session (if any) and immediately delete them
    result_ids = request.session.pop('result_ids', [])

    # Retrieve the People objects for the results
    results = People.objects.filter(id__in=result_ids)

    genders = People.objects.values_list('gender', flat=True).distinct()
    return render(request, 'ex10/search.html', {'genders': genders, 'results': results})