# Generated by Django 4.1 on 2022-09-30 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 18, 7, 22, 13627), verbose_name='date published'),
        ),
    ]
