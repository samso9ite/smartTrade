# Generated by Django 3.1.5 on 2021-01-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0005_sendfeedbackmodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/profImg'),
        ),
    ]