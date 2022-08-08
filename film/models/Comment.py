from django.contrib.auth import get_user_model
from django.db import models
from sqlalchemy import true
from .Movie import Movie

User = get_user_model()

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    