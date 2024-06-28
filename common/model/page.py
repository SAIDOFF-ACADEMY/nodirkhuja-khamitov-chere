from django.db import models
from django.utils.translation import gettext_lazy as _


from ckeditor.fields import RichTextField
class Page(models.Model):

    slug = models.SlugField()
    title = models.CharField(_('title'), max_length=100)
    content = RichTextField()


    def __str__(self) -> str:
        return self.title