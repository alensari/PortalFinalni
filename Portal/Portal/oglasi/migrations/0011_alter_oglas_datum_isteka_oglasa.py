# Generated by Django 3.2.7 on 2021-09-26 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oglasi', '0010_alter_oglas_datum_isteka_oglasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='datum_isteka_oglasa',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 9, 56, 37, 402373)),
        ),
    ]
