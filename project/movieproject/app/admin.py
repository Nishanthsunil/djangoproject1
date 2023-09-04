from django.contrib import admin
from .models import movie

class movieadmin(admin.ModelAdmin):
    list_display=("title",'image_preview','discription','year')
admin.site.register(movie,movieadmin)

