from django.shortcuts import render

def color_view(request):
    shades = [hex(i)[2:].zfill(2) for i in range(0, 256, 5)]  # Generate 50 shades for each color

    # Correctly generate color shades
    color_shades = {
        'black': ['#' + s*3 for s in shades],
        'red': ['#' + s + '0000' for s in shades],
        'green': ['#00' + s + '00' for s in shades],
        'blue': ['#0000' + s for s in shades],
    }

    colors = list(color_shades.keys())
    shades = list(zip(*color_shades.values()))

    return render(request, 'ex03/color_table.html', {'colors': colors, 'shades': shades})