# Generated by Django 4.0.3 on 2022-04-12 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='founder',
            options={'ordering': ['first_name'], 'verbose_name': 'Основатель', 'verbose_name_plural': 'Основатели'},
        ),
        migrations.AlterModelOptions(
            name='raiting',
            options={'ordering': ['value'], 'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['name'], 'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
    ]