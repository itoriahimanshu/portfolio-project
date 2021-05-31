from django.db import models

# Create your models here.
class Blog(models.Model):
     image = models.ImageField(upload_to = 'images/')
     title = models.CharField(max_length = 200)
     body = models.TextField()
     published_date = models.DateTimeField()


     def __str__(self):
         return self.title

     def summary(self):
         return self.body[:100]

     def published_date_pretty(self):
         return self.published_date.strftime('%b %e %Y')
