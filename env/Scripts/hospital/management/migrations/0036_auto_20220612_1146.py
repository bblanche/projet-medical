# Generated by Django 3.2.9 on 2022-06-12 10:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0035_auto_20220612_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.admins'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='validity',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 46, 38, 606864)),
        ),
    ]
