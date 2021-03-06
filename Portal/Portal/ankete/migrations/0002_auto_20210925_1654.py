# Generated by Django 3.2.7 on 2021-09-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankete', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_ankete', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='pitanja',
            old_name='tekst',
            new_name='pitanje',
        ),
        migrations.AlterField(
            model_name='pitanja',
            name='datum',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stavka',
            name='glasovi',
            field=models.PositiveSmallIntegerField(choices=[(1, 'U potunosti se ne slažem'), (2, 'Delimično se ne slažem'), (3, 'Niti se slažem, niti se ne slažem'), (4, 'Delimično se slažem'), (5, 'U potpunosti se slažem')], default=3),
        ),
    ]
