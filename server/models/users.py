from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

class User_Profile(models.Model):

    class Language(models.TextChoices):
        UZBEK = 'UZ', 'Uzbek'
        RUSSIAN = 'RU', 'Russian'
    
    user_id = models.CharField(max_length=200, primary_key=True)
    full_name = models.CharField(max_length=75)
    phone_number = PhoneNumberField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    language = models.CharField(max_length=2,
                                choices=Language.choices,
                                default=Language.UZBEK)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.full_name
