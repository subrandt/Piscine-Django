from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def execute_sql(sql):
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)

def init(request):
    sql = """
    CREATE TABLE ex02_movies (
        episode_nb INT PRIMARY KEY NOT NULL,
        title VARCHAR(64) NOT NULL,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
    );
    """
    success, result = execute_sql(sql)
    if success:
        return HttpResponse("OK")
    else:
        return HttpResponse(result)


def populate(request):
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        # Add the rest of the movies here
    ]
    for movie in movies:
        sql = f"""
        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
        VALUES {movie};
        """
        success, result = execute_sql(sql)
        if not success:
            return HttpResponse(result)
    return HttpResponse("OK")

def display(request):
    sql = "SELECT * FROM ex02_movies;"
    success, rows = execute_sql(sql)
    if success:
        if rows:
            html = '<table>'
            for row in rows:
                html += '<tr>'
                for field in row:
                    html += f'<td>{field}</td>'
                html += '</tr>'
            html += '</table>'
            return HttpResponse(html)
        else:
            return HttpResponse("No data available")
    else:
        return HttpResponse(rows)