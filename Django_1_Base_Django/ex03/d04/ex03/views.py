from django.shortcuts import render

def color_view(request):
    colors = ['black', 'red', 'blue', 'green']
    shades = [hex(i)[2:].zfill(2) for i in range(0, 256, 5)]  # Generate 50 shades for each color
    color_shades = {color: [(color + shade * (color != 'black')) for shade in shades] for color in colors}
    return render(request, 'ex03/color_table.html', {'color_shades': color_shades})
