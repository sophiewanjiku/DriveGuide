# Generated by Django 3.0.7 on 2024-02-09 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20240209_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='car',
            name='milage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='miles',
        ),
        migrations.RemoveField(
            model_name='car',
            name='no_of_owners',
        ),
        migrations.RemoveField(
            model_name='car',
            name='vin_no',
        ),
    ]