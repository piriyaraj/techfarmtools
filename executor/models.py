import json
from django.db import models

# Create your models here.
class Tiktoyt(models.Model):
    tiktok_id = models.CharField(unique=True, max_length=50)
    tiktok_last_video_id = models.CharField(unique=True, max_length=50)
    yt_name = models.CharField(max_length=500)
    yt_link = models.CharField(max_length=500)
    yt_title = models.CharField(max_length=500)
    yt_description = models.CharField(max_length=1000)
    yt_tags = models.CharField(max_length=500)
    yt_status = models.CharField(max_length=10, choices=[('private', 'Private'), ('public', 'Public')])
    yt_auth = models.FileField(upload_to='yt_auth/') # store the JSON file as a FileField
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    