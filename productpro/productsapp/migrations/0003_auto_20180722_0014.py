# Generated by Django 2.0.5 on 2018-07-22 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0002_auto_20180721_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pexfd',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 0, 14, 17, 671081)),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmfd',
            field=models.DateField(default=datetime.datetime(2018, 7, 22, 0, 14, 17, 671081)),
        ),
    ]
