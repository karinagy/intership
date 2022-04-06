# Generated by Django 4.0.3 on 2022-04-05 18:49

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['title'],
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
                ('city', models.CharField(max_length=255, null=True)),
                ('adress', models.CharField(help_text='Улица с номером дома', max_length=255, null=True)),
                ('contact', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Aвтосалон',
                'verbose_name_plural': 'Aвтосалоны',
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
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('value', models.IntegerField(default=1, validators=[core.validators.check_raiting])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_dealership.car')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Car_m2m_Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
                ('autoshop', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='car_dealership.car_dealership')),
                ('car', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='car_dealership.car')),
            ],
        ),
        migrations.AddField(
            model_name='car_dealership',
            name='cars',
            field=models.ManyToManyField(through='car_dealership.Car_m2m_Dealer', to='car_dealership.car'),
        ),
        migrations.AddField(
            model_name='car',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='car_dealership.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
