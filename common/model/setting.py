from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Setting(models.Model):

    telegram = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    longtitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    location_text = models.CharField(max_length=30)
    working_hours_start = models.TimeField(null=True, blank=True)
    working_hours_end = models.TimeField(null=True, blank=True)
    telegram_bot = models.CharField(max_length=30)

    def __str__(self) -> str:
        return 'Settings'