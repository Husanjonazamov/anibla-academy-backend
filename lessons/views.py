from rest_framework import generics
from .serializers import LessonListSerializer, LessonRetriveSerializer
from .models import Lesson
from rest_framework.response import Response

from rest_framework.views import APIView


class LessonsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()  # Barcha darslar
        serializer = LessonListSerializer(
            lessons, many=True, context={'request': request})
        return Response(serializer.data)


class LessonDetailAPIView(generics.RetrieveAPIView):
    """
    Darsning ID si orqali ma'lumotlarini olish uchun view
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonRetriveSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        lesson = self.get_object()
        serializer = self.get_serializer(lesson)
        return Response(serializer.data)
