from django.db import models

from helpers.change_homework import change_homework
from lessons.models import Lesson
from botusers.models import BotUser

# Create your models here.


class Homework(models.Model):
    IS_SUCCESS_CHOICES = [
        ('tekshirilmoqda', 'Tekshirilmoqda'),
        ('muvaffaqiyatli', 'Muvaffaqiyatli'),
        ('muvaffaqiyatsiz', 'Muvaffaqiyatsiz'),
    ]

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Kurs")
    user = models.ForeignKey(
        BotUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    send_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yuborilgan vaqt")
    is_successful = models.CharField(
        max_length=122, choices=IS_SUCCESS_CHOICES, default='tekshirilmoqda', verbose_name="Natija")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        change_homework(lesson=self.lesson, user=self.user,
                        is_successful=self.is_successful)

        # Super metodni chaqirish
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.user.name


class HomeWorkFiles(models.Model):

    file_type_choices = (
        ('video', 'Video'),
        ('file', 'Fayl'),
        ('photo', 'Rasm'),
        ('voice', 'Voice'),
    )

    homework = models.ForeignKey(
        Homework, on_delete=models.CASCADE, verbose_name="Uy vazifasi")
    file_id = models.URLField(max_length=250, verbose_name="Fayl ID")

    file_type = models.CharField(
        max_length=100, verbose_name="Fayl turi"
    )
