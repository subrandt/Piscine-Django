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

        # Check if min_date and max_date are empty
        if not min_date:
            min_date = '1900-01-01'  # Or any other default value
        if not max_date:
            max_date = datetime.now().strftime('%Y-%m-%d')  # Default to today's date

        if diameter:  # Check if diameter is not None or empty string
            diameter = int(diameter)  # Convert diameter to integer
        else:
            diameter = 0  # Default value if diameter is None or empty string

        results = People.objects.filter(
            gender=gender,
            movies__release_date__range=[min_date, max_date],
            homeworld__diameter__gte=diameter
        ).distinct()

        # Save the results in the session
        request.session['results'] = list(results.values())

    # Get the results from the session (if any) and immediately delete them
    results = request.session.pop('results', [])

    genders = People.objects.values_list('gender', flat=True).distinct()
    return render(request, 'ex10/search.html', {'genders': genders, 'results': results})