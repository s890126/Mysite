from django.db import models

# Create your models here.
class Home(models.Model):
    image = models.FilePathField(path="/img")
    description = models.TextField()
    skills = models.TextField()