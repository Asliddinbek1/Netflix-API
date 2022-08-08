from django.db import models

from .Actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    year = models.IntegerField(blank=False)
    imdb = models.IntegerField(default=1)
    genre = models.TextField()
    actors = models.ManyToManyField(Actor)
    
    def __str__(self) -> str:
        return f"{self.name}"