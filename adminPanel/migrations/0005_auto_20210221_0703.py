# Generated by Django 3.1.5 on 2021-02-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_auto_20210220_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardratemodel',
            name='rate',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
