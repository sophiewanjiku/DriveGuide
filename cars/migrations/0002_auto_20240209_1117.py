# Generated by Django 3.0.7 on 2024-02-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='modification_engine',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='powertrain_architecture',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='seats',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
    ]
