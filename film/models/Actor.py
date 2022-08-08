from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    birthdate = models.DateField(default="1950-01-01")
    genre = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"