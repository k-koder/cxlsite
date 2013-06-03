from django.db import models

# Create your models here.
class Author(models.Model):
    usern=models.CharField(max_length=30)
    passw=models.CharField(max_length=30)