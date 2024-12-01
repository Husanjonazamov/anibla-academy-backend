from django.db import models
from django.utils.timezone import now
from lessons.models import Lesson


class BotUser(models.Model):
    # Set user_id as the primary key
    user_id = models.BigIntegerField(
        primary_key=True, verbose_name="Telegram foydalanuvchi ID")
    name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Foydalanuvchi ismi")
    phone = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Telefon raqami")
    allowed_courses = models.ManyToManyField(
        Lesson, blank=True, verbose_name="Ruxsat etilgan kurslar")
    is_purchased = models.BooleanField(
        default=False, verbose_name="Sotib olinganmi?")
    purchase_time = models.DateTimeField(
        null=True, blank=True, verbose_name="Sotib olish vaqti")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_purchased and not self.purchase_time:
            self.purchase_time = now()
        super().save(*args, **kwargs)

        if self.is_purchased:
            from botusers.services import update_allowed_courses
            update_allowed_courses(self)
