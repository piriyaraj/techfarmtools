from django.contrib import admin

from facebook.models import Actress

# Register your models here.
@admin.register(Actress)
class gropsorAdmin(admin.ModelAdmin):
    list_display = ("instaid",'created',"modified")
    ordering = ('-modified',)
