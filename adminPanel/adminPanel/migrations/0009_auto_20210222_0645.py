# Generated by Django 3.1.5 on 2021-02-22 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0008_cardratemodel_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardratemodel',
            old_name='status',
            new_name='is_active',
        ),
    ]