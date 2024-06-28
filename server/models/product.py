from ckeditor.fields import RichTextField

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=70)
    content = RichTextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
    