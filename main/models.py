from django.db import models


class ImageGallery(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='main/static/images/media')

