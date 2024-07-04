# Generated by Django 4.2.1 on 2024-07-03 11:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('content', ckeditor.fields.RichTextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=75)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('UZ', 'Uzbek'), ('RU', 'Russian')], default='UZ', max_length=2)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('free_count', models.PositiveIntegerField()),
                ('latitude', models.FloatField(max_length=100)),
                ('longtitude', models.FloatField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status_changed_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('WA', 'Waiting'), ('PR', 'Process'), ('CD', 'Completed')], default='WA', max_length=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.user_profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='server.user_profile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='server.product')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
