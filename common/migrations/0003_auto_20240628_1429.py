# Generated by Django 4.2.1 on 2024-06-28 14:29

from django.db import migrations
from common.model.setting import Setting

def create_settings(*args, **kwargs):

    Setting.objects.create(
        telegram='bot-chere',
        phone_number="+998978824042",
        longtitude=1,
        latitude=1,
        location_text='bot',
        working_hours_start='00:00:00',
        working_hours_end='23:59:59',
        telegram_bot='chere_bot',

    )


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
    ]
    atomic=False
    operations = [
        migrations.RunPython(create_settings)
    ]