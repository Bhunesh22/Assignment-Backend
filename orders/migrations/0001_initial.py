# Generated by Django 4.2.7 on 2023-11-12 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradingsymbol', models.CharField(blank=True, max_length=100, null=True)),
                ('exchange', models.CharField(blank=True, max_length=100, null=True)),
                ('isin', models.IntegerField(blank=True, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('authorised_date', models.CharField(blank=True, max_length=100, null=True)),
                ('average_price', models.FloatField(blank=True, null=True)),
                ('last_price', models.FloatField(blank=True, null=True)),
                ('close_price', models.FloatField(blank=True, null=True)),
                ('pnl', models.FloatField(blank=True, null=True)),
                ('day_change', models.FloatField(blank=True, null=True)),
                ('day_change_percentage', models.FloatField(blank=True, null=True)),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
