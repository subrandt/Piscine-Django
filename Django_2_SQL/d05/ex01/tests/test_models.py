from django.test import TestCase
from ex01.models import Movies

class MoviesModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Movies.objects.create(title='Test Movie', episode_nb=1, director='Test Director', producer='Test Producer', release_date='2000-01-01')

    def test_title_label(self):
        movie = Movies.objects.get(id=1)
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        movie = Movies.objects.get(id=1)
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length, 64)

    def test_director_max_length(self):
        movie = Movies.objects.get(id=1)
        max_length = movie._meta.get_field('director').max_length
        self.assertEquals(max_length, 32)

    def test_producer_max_length(self):
        movie = Movies.objects.get(id=1)
        max_length = movie._meta.get_field('producer').max_length
        self.assertEquals(max_length, 128)

    def test_episode_nb_primary_key(self):
        movie = Movies.objects.get(id=1)
        primary_key = movie._meta.pk.name
        self.assertEquals(primary_key, 'episode_nb')

    def test_str_method(self):
        movie = Movies.objects.get(id=1)
        self.assertEquals(str(movie), movie.title)

    def test_create_and_retrieve_movie(self):
        Movies.objects.create(title='Test Movie 2', episode_nb=2, director='Test Director 2', producer='Test Producer 2', release_date='2000-01-02')
        movie = Movies.objects.get(episode_nb=2)
        self.assertEquals(movie.title, 'Test Movie 2')
        self.assertEquals(movie.director, 'Test Director 2')
   