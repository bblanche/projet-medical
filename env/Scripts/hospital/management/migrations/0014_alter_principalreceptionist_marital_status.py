# Generated by Django 3.2.9 on 2022-03-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_alter_patients_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principalreceptionist',
            name='marital_status',
            field=models.CharField(choices=[('', 'SINGLE'), ('SINGLE', 'SINGLE'), ('MARRIED', 'MARRIED')], max_length=8),
        ),
    ]
