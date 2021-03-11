# Generated by Django 3.1.5 on 2021-03-11 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0021_auto_20210311_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='referral_code',
            field=models.CharField(default=uuid.uuid4, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='referred_by',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
