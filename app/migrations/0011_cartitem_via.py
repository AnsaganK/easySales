# Generated by Django 5.0.6 on 2024-05-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='via',
            field=models.CharField(choices=[('site', 'Сайт'), ('telegram', 'Телеграм')], default='site', max_length=64),
        ),
    ]