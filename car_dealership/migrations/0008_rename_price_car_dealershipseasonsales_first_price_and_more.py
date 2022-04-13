# Generated by Django 4.0.3 on 2022-04-13 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealership', '0007_alter_car_dealershipseasonsales_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_dealershipseasonsales',
            old_name='price',
            new_name='first_price',
        ),
        migrations.AddField(
            model_name='car_dealershipseasonsales',
            name='now_price',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_dealershipseasonsales',
            name='start_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
