from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def execute_sql(sql):
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            if sql.strip().upper().startswith('SELECT'):
                return True, cursor.fetchall()
            else:
                return True, None
        except Exception as e:
            return False, str(e)

def init(request):
    sql = """
    CREATE TABLE IF NOT EXISTS ex02_movies (
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
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]
    for movie in movies:
        sql_check = f"SELECT * FROM ex02_movies WHERE episode_nb = {movie[0]};"
        success, result = execute_sql(sql_check)
        if success and result:
            continue  # Skip this movie if it already exists
        sql_insert = f"""
        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
        VALUES {movie};
        """
        success, result = execute_sql(sql_insert)
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