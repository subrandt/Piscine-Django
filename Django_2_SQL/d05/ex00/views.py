from django.shortcuts import render

from django.http import HttpResponse
import psycopg2

def init(request):
    try:
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) NOT NULL UNIQUE,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)
        conn.commit()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)