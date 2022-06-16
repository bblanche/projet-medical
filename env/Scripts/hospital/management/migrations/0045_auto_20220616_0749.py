# Generated by Django 3.2.9 on 2022-06-16 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0044_alter_payments_validity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmotif',
            old_name='duree_en_jours',
            new_name='validity',
        ),
        migrations.AlterField(
            model_name='payments',
            name='validity',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 7, 48, 57, 662416)),
        ),
    ]