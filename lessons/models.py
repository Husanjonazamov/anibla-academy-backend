from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Dars nomi")
    description = models.TextField(verbose_name="Dars tavsifi")
    date = models.DateField(verbose_name="Dars sanasi")
    start_date = models.IntegerField(
        null=True, blank=True, verbose_name="Boshlanish sanasi")

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'

    def __str__(self):
        return self.title


class Voice(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Dars")
    voice_id = models.CharField(max_length=100, verbose_name="Ovoz ID")

    class Meta:
        verbose_name = 'Ovoz'
        verbose_name_plural = 'Ovozlar'


class Photo(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Dars")
    photo_id = models.CharField(max_length=100, verbose_name="Rasm ID")

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'


class Video(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Dars")
    vide_id = models.CharField(max_length=100, verbose_name="Video ID")

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'


class File(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Dars")
    file_id = models.CharField(max_length=100, verbose_name="Fayl ID")

    class Meta:
        verbose_name = 'Fayl'
        verbose_name_plural = 'Fayllar'
