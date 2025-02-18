# Generated by Django 5.1.2 on 2024-11-28 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('botusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botusers.botuser')),
            ],
        ),
    ]
