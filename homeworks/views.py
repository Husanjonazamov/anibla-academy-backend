from rest_framework import generics
from .serializers import HomeworksSeralizers
from .models import Homework


class HomeworkListCreateView(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworksSeralizers
