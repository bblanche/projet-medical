# Generated by Django 3.2.9 on 2022-03-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_rename_proche_phone_patients_emergency_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(choices=[('MAN', 'MAN'), ('WOMAN', 'WOMAN')], max_length=5, null=True),
        ),
    ]
