from django.shortcuts import render

def index(request):
    cheatsheet = [
        ('Headers', '# This is an <h1> tag\n## This is an <h2> tag\n###### This is an <h6> tag'),
        ('Emphasis', '*This text will be italic*\n_This will also be italic_\n**This text will be bold**\n__This will also be bold__'),
        ('Lists', '1. Item 1\n2. Item 2\n3. Item 3\n   * Item 3a\n   * Item 3b'),

    ]
    return render(request, "ex00", {'cheatsheet': cheatsheet})
