from rest_framework import serializers

from homeworks.models import Homework
from .models import Lesson, Video, File, Photo, Voice
from botusers.models import BotUser

from datetime import timedelta
from django.utils.timezone import now
from django.utils import timezone


class LessonListSerializer(serializers.ModelSerializer):
    is_access = serializers.SerializerMethodField()

    def get_is_access(self, obj):
        user_id = self.context['request'].query_params.get('user_id', None)
        if user_id is None:
            return False

        user = BotUser.objects.filter(user_id=user_id).first()
        if user is None or not user.is_purchased:
            return False

        first_lesson = Lesson.objects.order_by('start_date').first()
        if obj == first_lesson:
            return True

        access_time = user.purchase_time + timedelta(hours=obj.start_date or 0)
        access_time = timezone.localtime(access_time)
        print(f"Dars '{obj.title}' ochiladi {
              access_time.strftime('%Y-%m-%d %H:%M:%S')} da")

        if timezone.localtime(now()) >= access_time:
            user.allowed_courses.add(obj)
            return True

        return False

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonRetriveSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    voices = serializers.SerializerMethodField()
    is_lesson_homework_status = serializers.SerializerMethodField()

    def get_is_lesson_homework_status(self, obj):
        user_id = self.context['request'].query_params.get('user_id', None)
        if user_id is None:
            return False
        user = BotUser.objects.filter(user_id=user_id).first()
        if user is None:
            return False

        user_lesson_homework = Homework.objects.filter(
            user=user,
            lesson=obj,
        )

        if user_lesson_homework.exists():
            print(user_lesson_homework)
            return user_lesson_homework.first().is_successful

        return 'topshirilmagan'

    def get_voices(self, obj):
        voices = Voice.objects.filter(lesson=obj.id).values()
        return voices

    def get_videos(self, obj):
        videos = Video.objects.filter(lesson=obj.id).values()
        return videos

    def get_files(self, obj):
        files = File.objects.filter(lesson=obj.id).values()
        return files

    def get_photos(self, obj):
        photos = Photo.objects.filter(lesson=obj.id).values()
        return photos

    class Meta:
        model = Lesson
        fields = '__all__'
