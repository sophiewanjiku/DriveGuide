# Generated by Django 3.0.7 on 2024-02-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20240209_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Emission_standard',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='Weight_to_power_ratio',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='Weight_to_torque_ratio',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='assisting_systems',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='drive_wheel',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='engine_aspiration',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='engine_oil_capacity',
            field=models.CharField(default='unkown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='front_brakes',
            field=models.CharField(default='uknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='front_suspension',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_system',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='gears',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='minimum_speed',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='power_steering',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='rear_brakes',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='rear_suspension',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='steering_type',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='tank_capacity',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='tire_size',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
    ]
