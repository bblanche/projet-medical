# Generated by Django 3.2.9 on 2022-01-30 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20220130_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmotif',
            old_name='montant',
            new_name='amount_motif',
        ),
    ]