# Generated by Django 3.0.7 on 2024-03-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20240304_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='acceleration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_system',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
