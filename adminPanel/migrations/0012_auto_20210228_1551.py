# Generated by Django 3.1.5 on 2021-02-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0011_auto_20210227_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardratemodel',
            name='rate',
            field=models.CharField(max_length=220),
        ),
    ]
