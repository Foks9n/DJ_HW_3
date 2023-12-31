# Generated by Django 3.1.2 on 2023-09-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Цена')),
                ('image', models.CharField(max_length=256, verbose_name='URL изображения')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.SlugField(max_length=64)),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
    ]
