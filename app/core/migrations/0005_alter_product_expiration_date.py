# Generated by Django 4.2.12 on 2024-07-12 01:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 1, 34, 1, 203629, tzinfo=datetime.timezone.utc), verbose_name='Caducidad'),
        ),
    ]