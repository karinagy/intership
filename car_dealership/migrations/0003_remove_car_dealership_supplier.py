# Generated by Django 4.0.3 on 2022-04-03 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealership', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_dealership',
            name='supplier',
        ),
    ]
