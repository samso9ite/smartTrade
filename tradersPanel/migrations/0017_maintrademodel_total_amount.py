# Generated by Django 3.1.5 on 2021-02-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0016_auto_20210227_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintrademodel',
            name='total_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]