# Generated by Django 4.0.3 on 2022-04-03 12:37

import core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchaser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('year', models.IntegerField(null=True)),
                ('price', models.IntegerField(default=12000)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')], default='USD', max_length=3)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Out of stock', 'Out Of Stock'), ('Withdrawn from sale', 'Withdrawn From Sale')], default='Available', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rewiew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=255)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_rewiew', to='car_dealership.car')),
                ('purchaser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchaser_rewiew', to='purchaser.purchaser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('value', models.IntegerField(default=9, validators=[core.validators.check_raiting])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carreating', to='car_dealership.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car_dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('characteristic', models.TextField(blank=True)),
                ('location', django_countries.fields.CountryField(max_length=2, null=True)),
                ('contact', models.EmailField(max_length=254)),
                ('car', models.ManyToManyField(to='car_dealership.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
