from django.contrib import admin

from facebook.models import Actress,Metadata

# Register your models here.
@admin.register(Actress)
class gropsorAdmin(admin.ModelAdmin):
    list_display = ("instaid",'created',"modified")
    ordering = ('-modified',)
    
@admin.register(Metadata)
class metaAdmin(admin.ModelAdmin):
    list_display = ("name","key","pageId",'created',"modified")
    list_display_links = ('name',)
    list_editable=["key","pageId"]
    ordering = ('-modified',)

