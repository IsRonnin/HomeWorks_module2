# Generated by Django 4.1.7 on 2023-03-14 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('image', models.ImageField(upload_to='categories', verbose_name='изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='имя')),
                ('price', models.CharField(max_length=100, verbose_name='цена')),
                ('animal', models.CharField(max_length=100, verbose_name='животное')),
                ('weight', models.CharField(max_length=100, verbose_name='вес')),
                ('release_date', models.DateField(verbose_name='дата производства')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoomag.category', verbose_name='категория')),
            ],
        ),
    ]
