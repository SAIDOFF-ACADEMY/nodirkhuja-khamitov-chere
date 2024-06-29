from common.model.setting import TimeAbstract
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(TimeAbstract):

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


class FreeProduct(TimeAbstract):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    free_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.name