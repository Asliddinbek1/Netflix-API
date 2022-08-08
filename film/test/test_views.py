from urllib import response
from django.test import Client, TestCase

from film.models.Actor import Actor
from film.models.Movie import Movie


class TestActorViewSet(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name = "Test_Actor 1",  genre = "Test_Genre_1")
        
        self.movie_1 = Movie.objects.create(name = "Test_Movie_1", year = 2012, genre = "Test_Movie_genre_1")
        self.movie_2 = Movie.objects.create(name = "Test_Movie_2", year = 2019, genre = "Test_Movie_genre_2" )
        self.movie_3 = Movie.objects.create(name = "Test_Movie_3", year = 2020, genre = "Test_Movie_genre_1" )
        self.movie_4 = Movie.objects.create(name = "Test_Movie_4", year = 2012, genre = "Test_Movie_genre_4" )
        self.movie_5 = Movie.objects.create(name = "Test_Movie_5", year = 2012, genre = "Test_Movie_genre_1" )


        self.client = Client()
        
    # def test_get_all_movie(self):
    #     response = self.client.get("movie")

    def test_get_all_actor(self):
        response = self.client.get('/actor/')
        data = response.data

        self.assertEquals(len(data), 1)
    
    def test_get_all_movie(self):
        response = self.client.get("/movie/")
        data = response.data

        self.assertEquals(len(data), 5)
    
    def test_movie_fillter(self):
        response = self.client.get("/movie/?search=Test_Movie_genre_1")
        data = response.data
        
        self.assertEquals(response.status_code, 200)

        self.assertEquals(len(data), 3)

    def test_movie_order(self):
        response = self.client.get("/movie/")
        data = response.data
        
        self.assertEquals(response.status_code, 200)

        self.assertEquals(len(data), 5)

    