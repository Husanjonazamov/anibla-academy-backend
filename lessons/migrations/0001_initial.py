# Generated by Django 5.1.2 on 2024-11-28 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Dars nomi')),
                ('description', models.TextField(verbose_name='Dars tavsifi')),
                ('date', models.DateField(verbose_name='Dars sanasi')),
                ('start_date', models.IntegerField(blank=True, null=True, verbose_name='Boshlanish sanasi')),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=100, verbose_name='Fayl ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': 'Fayl',
                'verbose_name_plural': 'Fayllar',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_id', models.CharField(max_length=100, verbose_name='Rasm ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': 'Rasm',
                'verbose_name_plural': 'Rasmlar',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vide_id', models.CharField(max_length=100, verbose_name='Video ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videolar',
            },
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_id', models.CharField(max_length=100, verbose_name='Ovoz ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': 'Ovoz',
                'verbose_name_plural': 'Ovozlar',
            },
        ),
    ]
