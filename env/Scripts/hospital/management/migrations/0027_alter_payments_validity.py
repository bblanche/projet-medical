# Generated by Django 3.2.9 on 2022-03-09 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_alter_payments_validity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='validity',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 9, 11, 14, 18, 797801)),
        ),
    ]
