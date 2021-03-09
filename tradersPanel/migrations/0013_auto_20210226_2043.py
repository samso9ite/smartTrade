# Generated by Django 3.1.5 on 2021-02-26 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tradersPanel', '0012_auto_20210226_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trademodel',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='trademodel',
            name='status',
        ),
        migrations.RemoveField(
            model_name='trademodel',
            name='user',
        ),
        migrations.CreateModel(
            name='MainTradeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default=uuid.uuid4, max_length=255, unique=True)),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Success'), ('3', 'Failed')], default='1', max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trademodel',
            name='trade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersPanel.maintrademodel'),
        ),
    ]