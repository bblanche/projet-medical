# Generated by Django 3.2.9 on 2022-06-16 08:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0048_alter_paymentmotif_date_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='department',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='patient',
        ),
        migrations.AddField(
            model_name='payments',
            name='patientDepartment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.patientdepartments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymentmotif',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 9, 24, 51, 977316)),
        ),
    ]
