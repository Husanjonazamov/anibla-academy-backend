# Generated by Django 5.1.3 on 2024-11-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeworks", "0002_alter_homeworkfiles_file_id_homework_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homeworkfiles",
            name="file_type",
            field=models.CharField(default=1, max_length=100, verbose_name="Fayl turi"),
            preserve_default=False,
        ),
    ]
