from django.shortcuts import render

def index(request):
    cheatsheet = [
        ('Headers', '#', '# This is an <h1> tag\n## This is an <h2> tag\n###### This is an <h6> tag'),
        ('Emphasis', '*', '*This text will be italic*'),
        ('Emphasis', '_', '_This will also be italic_'),
        ('Emphasis', '**', '**This text will be bold**'),
        ('Emphasis', '__', '__This will also be bold__'),
        ('Lists', '1.', '1. Item 1\n2. Item 2\n3. Item 3'),
        ('Lists', '*', '* Item 1\n* Item 2\n* Item 3'),
        ('Links', '[Link Text](URL)', '[This is a link](http://www.example.com)'),
        ('Images', '![Alt Text](URL)', '![This is an image](http://www.example.com/image.jpg)'),
        ('Code', '`code`', '`This is inline code`'),
        ('Code Block', '```code```', '```\nThis is a code block\n```'),
        ('Blockquotes', '> quote', '> This is a blockquote'),
        ('Horizontal Rule', '---', '---'),
        ('Table', '| Header |', '| Header 1 | Header 2 |\n| --- | --- |\n| Cell 1 | Cell 2 |'),
        ('Strikethrough', '~~text~~', '~~This text is strikethrough~~'),
        ('Task List', '- [x] or - [ ]', '- [x] This is a complete item\n- [ ] This is an incomplete item'),
    ]
    return render(request, "index.html", {'cheatsheet': cheatsheet})
