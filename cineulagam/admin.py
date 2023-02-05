from unittest import result
from django.contrib import admin
from cineulagam.models import Post

@admin.register(Post)
class gropsorAdmin(admin.ModelAdmin):
    list_display = ("link",'created',"modified","extract")
    list_editable=['extract']
    ordering = ('-created',)
