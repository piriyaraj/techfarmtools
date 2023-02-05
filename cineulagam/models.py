from django.db import models

# Create your models here.
class Post(models.Model):
    link = models.URLField(max_length=1000,unique=True)
    extract=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now_add=True)