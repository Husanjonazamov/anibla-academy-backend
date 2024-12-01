from django.shortcuts import get_object_or_404
from .serializers import UserSerializers
from rest_framework import generics
from lessons.models import Lesson

from botusers.models import BotUser


class GetBotUsersView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        new_user = serializer.save()
        first_lesson = Lesson.objects.first()
        if first_lesson:
            new_user.allowed_courses.add(first_lesson)


class GetBotUserIDView(generics.RetrieveUpdateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(BotUser.objects.filter(user_id=user_id))
