# Generated by Django 3.1.5 on 2021-02-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0010_testimonialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
