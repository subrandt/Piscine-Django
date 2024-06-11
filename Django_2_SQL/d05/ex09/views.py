from django.shortcuts import render
from .models import People, Planets

def display(request):
    data = People.objects.filter(homeworld__climate__contains='windy').order_by('name')
    if not data:
        return render(request, 'ex09/no_data.html')
    return render(request, 'ex09/display.html', {'data': data})