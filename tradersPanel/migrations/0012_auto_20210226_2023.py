# Generated by Django 3.1.5 on 2021-02-26 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0010_auto_20210222_0809'),
        ('tradersPanel', '0011_testimonialmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trademodel',
            name='trade_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminPanel.cardratemodel'),
        ),
    ]