from django.db import models

class GalleryPhoto(models.Model):
    photo = models.ImageField(upload_to='gallery/%Y/%m', null=True, blank=True)

   