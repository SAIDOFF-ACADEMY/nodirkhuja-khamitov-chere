# Generated by Django 4.2.1 on 2024-06-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20240628_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/%Y/%m'),
        ),
    ]