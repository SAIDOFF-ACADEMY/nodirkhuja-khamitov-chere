import os
import hashlib

from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings
from django.db import models

class Phone_Token(models.Model):

    class Language(models.TextChoices):
        UZBEK = 'UZ', 'Uzbek'
        RUSSIAN = 'RU', 'Russian'

    user_id = models.CharField(max_length=200, primary_key=True)
    phone_number = PhoneNumberField(unique=True)
    otp = models.CharField(max_length=4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2,
                                choices=Language.choices,
                                default=Language.UZBEK)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.full_name
    

    @classmethod
    def generate_otp(cls,length=4):
        hash_algorithm = getattr(settings,"PHONE_LOGIN_OTP_HASH_ALGORITHM","sha256")
        m=getattr(hashlib,hash_algorithm)()
        m.update(getattr(settings,'SECRET_KEY',None).encode('utf-8'))
        m.update(os.urandom(16))
        otp = str(int(m.hexdigest(),16))[-length:]
        return otp