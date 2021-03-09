# Generated by Django 3.1.5 on 2021-02-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0015_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintrademodel',
            name='bank_accnt_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='maintrademodel',
            name='bank_accnt_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='maintrademodel',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='maintrademodel',
            name='default_bank_details',
            field=models.BooleanField(default=False),
        ),
    ]