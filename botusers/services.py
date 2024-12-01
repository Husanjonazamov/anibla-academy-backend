from datetime import timedelta
from django.utils.timezone import now
from lessons.models import Lesson


def update_allowed_courses(user):
    """
    Foydalanuvchi sotib olgan darslarni start_date asosida 'allowed_courses'ga qo‘shadi.
    """
    if not user.purchase_time:
        return

    lessons = Lesson.objects.all()

    for lesson in lessons:
        access_time = user.purchase_time + \
            timedelta(minutes=lesson.start_date or 0)

        if now() >= access_time:
            user.allowed_courses.add(lesson)
        else:
            print(f"{lesson.title} hali ochilmadi.")
