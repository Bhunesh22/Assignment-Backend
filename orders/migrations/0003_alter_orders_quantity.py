# Generated by Django 4.2.7 on 2023-11-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_isin_alter_orders_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
