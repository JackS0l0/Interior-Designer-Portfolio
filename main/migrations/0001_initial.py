# Generated by Django 5.1.5 on 2025-02-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(default='none', verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'О нас на футере',
                'verbose_name_plural': 'О нас на футере',
            },
        ),
        migrations.CreateModel(
            name='HeaderBackgroud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(default='none')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='MainTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('float1', models.CharField(default='none', max_length=200, verbose_name='Текст 1')),
                ('float2', models.CharField(default='none', max_length=200, verbose_name='Текст 2')),
                ('float3', models.CharField(default='none', max_length=200, verbose_name='Текст 3')),
                ('about', models.TextField(default='none', verbose_name='О нас')),
                ('addressTxt', models.CharField(default='none', max_length=200, verbose_name='Адрес')),
                ('addressUrl', models.URLField(default='none', verbose_name='Ссылка')),
                ('phone', models.CharField(default='none', max_length=200, verbose_name='Телефон')),
                ('whatsapp', models.CharField(default='none', max_length=200, verbose_name='Телефон')),
                ('telegram', models.CharField(default='none', max_length=200, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('img', models.URLField(default='none')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]
