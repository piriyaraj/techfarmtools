from django.contrib import admin
from tiktoktools.models import Tiktofb

# Register your models here.
@admin.register(Tiktofb)
class metaAdmin(admin.ModelAdmin):
    list_display = ("tiktok_id","tiktok_last_video_id","fb_page_name","fb_page_id",'page_access_token')
    list_display_links = ('fb_page_name',)
    list_editable=["page_access_token"]
    ordering = ('-modified',)