# Generated by Django 3.2.9 on 2022-06-16 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0049_auto_20220616_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmotif',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 10, 11, 1, 268513)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='valid',
            field=models.DateTimeField(),
        ),
    ]
