from django.contrib import admin

from film.models.Comment import Comment
from .models import Actor, Movie
# Register your models here.


admin.site.register([Actor, Movie, Comment])


