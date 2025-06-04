from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):  # this helps in representing the object as a string
        return f"{self.title} by {self.author} ({self.published_date})"
