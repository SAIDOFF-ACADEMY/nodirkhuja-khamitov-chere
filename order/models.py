from phonenumber_field.modelfields import PhoneNumberField

from user.models import User
from product.models import Product
from common.model.base_model import BaseModel

from django.db import models
from django.utils.translation import gettext_lazy as _

class Orders(BaseModel):

    class Status(models.TextChoices):
        WAITING = 'WA', _('Waiting')
        PROCESS = 'PR', _('Process')
        COMPLETED = 'CD', _('Completed')

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='user_orders')
    count = models.PositiveIntegerField(_('count'))
    free_count = models.PositiveIntegerField("")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    latitude = models.FloatField(max_length=100)
    longtitude = models.FloatField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    quantity = models.PositiveIntegerField(default=0)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    status_changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                              choices=Status.choices, 
                              default=Status.WAITING)
    
    admin = models.ForeignKey(User, on_delete=models.PROTECT, related_name='admin_users')



    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.product.name
