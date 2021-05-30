from django.db import models

# Create your models here.
class Blog(models.Model):
     image = models.ImageField(upload_to = 'images/')
     title = models.CharField(max_length = 200)
     body = models.TextField()
     published_date = models.DateTimeField()
