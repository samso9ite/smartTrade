# Generated by Django 3.1.5 on 2021-02-21 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0006_auto_20210221_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradecardtypemodel',
            name='price',
        ),
    ]
