from phonenumber_field.modelfields import PhoneNumberField

from .users import User_Profile
from .product import Product

from django.db import models

class Orders(models.Model):

    class Status(models.TextChoices):
        WAITING = 'WA', 'Waiting'
        PROCESS = 'PR', 'Process'
        COMPLETED = 'CD', 'Completed'

    owner = models.ForeignKey(User_Profile,
                              on_delete=models.CASCADE,
                              related_name='user_orders')
    count = models.PositiveIntegerField()
    free_count = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    latitude = models.FloatField(max_length=100)
    longtitude = models.FloatField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    quantity = models.PositiveIntegerField(default=0)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status_changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                              choices=Status.choices, 
                              default=Status.WAITING)
    
    admin = models.ForeignKey(User_Profile, on_delete=models.PROTECT)



    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.Product_Type.name
