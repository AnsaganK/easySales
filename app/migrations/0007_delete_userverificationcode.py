# Generated by Django 5.0.6 on 2024-05-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_userverificationcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserVerificationCode',
        ),
    ]
