from unittest import result
from django.contrib import admin
from wordpress.models import Nammacinema_post

@admin.register(Nammacinema_post)
class gropsorAdmin(admin.ModelAdmin):
    list_display = ("link",'created',"modified","extract")
    list_editable=['extract']
    ordering = ('-created',)
