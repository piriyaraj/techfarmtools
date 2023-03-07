from django.contrib import admin

from executor.models import Tiktoyt

# Register your models here.
@admin.register(Tiktoyt)
class metaAdmin(admin.ModelAdmin):
    list_display = ("yt_name","tiktok_id","tiktok_last_video_id","yt_link",'yt_auth')
    list_display_links = ('yt_name',)
    list_editable=["tiktok_id","tiktok_last_video_id","yt_link",'yt_auth']
    ordering = ('-modified',)