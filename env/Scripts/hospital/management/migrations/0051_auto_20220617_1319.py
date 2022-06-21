# Generated by Django 3.2.9 on 2022-06-17 12:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0050_auto_20220616_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='service_receptionist',
        ),
        migrations.AddField(
            model_name='parameters',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.nurse'),
        ),
        migrations.AlterField(
            model_name='paymentmotif',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 13, 19, 54, 809233)),
        ),
    ]