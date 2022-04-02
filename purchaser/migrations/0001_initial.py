# Generated by Django 4.0.3 on 2022-04-02 21:06

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('age', models.IntegerField()),
                ('birth', models.DateField(null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=13, null=True, validators=[core.validators.check_phonenum])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]