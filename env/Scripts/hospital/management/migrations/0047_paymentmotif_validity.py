# Generated by Django 3.2.9 on 2022-06-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0046_auto_20220616_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmotif',
            name='validity',
            field=models.CharField(default=14, max_length=9999999999),
            preserve_default=False,
        ),
    ]