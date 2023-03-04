from django.contrib import admin

from facebooktools.models import Actress, Facebook_group,Metadata

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

@admin.register(Facebook_group)
class Facebook_groupAdmin(admin.ModelAdmin):
    list_display = ('created',"name","groupId","modified")
    # list_display_links = ()
    list_editable=["groupId","name"]
    ordering = ('-modified',)