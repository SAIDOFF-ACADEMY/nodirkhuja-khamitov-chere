from django.db import models
from datetime import datetime

class BaseModel(models.Model):

    created_at = models.DateField(auto_now_add=datetime.now)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True