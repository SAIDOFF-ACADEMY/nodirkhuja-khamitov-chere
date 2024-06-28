from datetime import datetime

from django.db import models

class GalleryPhoto(models.Model):
    photo = models.ImageField(upload_to='self.upload_to', null=True, blank=True)


    @staticmethod
    def upload_to(instance):
        now = datetime.now()
        return f'/media/gallery/{now.year}/{now.month}'