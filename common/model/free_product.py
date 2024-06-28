from django.db import models
from product.models import Product


class FreeProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    free_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.name