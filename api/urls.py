from django.urls import path
from botusers.views import GetBotUsersView, GetBotUserIDView
from lessons.views import LessonsListAPIView, LessonDetailAPIView
from homeworks.views import HomeworkListCreateView

urlpatterns = [
    # bot users
    path('users/', GetBotUsersView.as_view(), name='users'),
    path('users/<int:pk>/', GetBotUserIDView.as_view(), name='users_id'),

    # lessons views
    path('lessons/', LessonsListAPIView.as_view(), name='lessons-list-create'),
    path('lessons/<int:id>/', LessonDetailAPIView.as_view(), name='lesson-detail'),

    # homework views
    path('homework/', HomeworkListCreateView.as_view(), name='homework-list'),
]
