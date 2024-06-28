from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from django.utils import timezone

class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User_Profile(AbstractUser):
    class Language(models.TextChoices):
        UZBEK = 'UZ', 'Uzbek'
        RUSSIAN = 'RU', 'Russian'
    
    username = None
    first_name = None
    last_name = None
    telegram_id = models.CharField(max_length=200)
    full_name = models.CharField(max_length=75)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True, error_messages={
        _("unique"): _("email must be unique") 
    })
    created_at = models.DateTimeField(auto_now_add=True)


    language = models.CharField(max_length=2,
                                choices=Language.choices,
                                default=Language.UZBEK)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.email
