# Generated by Django 5.0.6 on 2024-05-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]
