from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2) or "0.00"
    # image = models.ImageField(upload_to="book_images/", blank=True, null=True) or None

    def __str__(self):  # this helps in representing the object as a string
        return f"{self.title} by {self.author} ({self.published_date})"
