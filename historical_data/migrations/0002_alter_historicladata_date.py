# Generated by Django 4.2.7 on 2023-11-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicladata',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
