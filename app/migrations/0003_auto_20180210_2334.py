# Generated by Django 2.0.2 on 2018-02-10 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180210_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='call',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name='Conversation Time'),
        ),
    ]