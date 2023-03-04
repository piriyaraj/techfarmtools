from django.db import models

# Create your models here.
class Tiktofb(models.Model):
    tiktok_id=models.CharField(unique=True, max_length=50)
    tiktok_last_video_id=models.CharField(unique=True, max_length=50)
    fb_page_name=models.CharField(max_length=500)
    fb_page_id=models.CharField(max_length=500)
    page_access_token=models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)