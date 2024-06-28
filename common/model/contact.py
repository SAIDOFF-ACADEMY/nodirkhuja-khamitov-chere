from django.db import models
from user.models import User_Profile
from django.utils.translation import gettext_lazy as _

class UserContact(models.Model):

    full_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.full_name} from telegram: {self.user.telegram_id != None}' 
    
    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')