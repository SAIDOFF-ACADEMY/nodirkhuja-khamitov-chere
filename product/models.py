from common.model.base_model import BaseModel

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class Product(BaseModel):

    name = models.CharField(max_length=70)
    content = RichTextUploadingField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class FreeProduct(BaseModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    free_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.name
    
    @classmethod
    def discount(cls, quantity, product):
        product = Product.objects.get(Q(name_uz=product) | Q(name_ru=product))
        free = cls.objects.filter(product=product).order_by('-count')
        free_count = 0
        for f in free:
            if quantity >= f.count:
                return f.free_count
        return free_count