# Generated by Django 3.1.5 on 2021-02-26 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradersPanel', '0014_auto_20210226_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='trade_card')),
                ('trade_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradersPanel.trademodel')),
            ],
            options={
                'verbose_name': 'ImageModel',
                'verbose_name_plural': 'ImageModels',
                'db_table': 'images',
                'managed': True,
            },
        ),
    ]