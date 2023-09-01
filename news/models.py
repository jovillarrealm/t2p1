from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField(default= "Nada ha pasado")
    date = models.DateField(default="2000-12-13")
    def __str__(self):
        return self.headline