# Generated by Django 3.2.9 on 2022-03-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20220303_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmotif',
            name='durée_en_jours',
            field=models.CharField(default=14, max_length=999999),
            preserve_default=False,
        ),
    ]
