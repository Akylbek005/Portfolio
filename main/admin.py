from django.contrib import admin
from .models import *


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


