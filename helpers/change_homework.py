

from botusers.models import BotUser
from helpers.send_message_user import send_message
from lessons.models import Lesson


def change_homework(lesson: Lesson, user: BotUser, is_successful: bool):

    # Agar uyga vazifa muvaffaqiyatli bo'lsa
    if is_successful == 'muvaffaqiyatli':
        next_lesson = Lesson.objects.filter(id=lesson.id + 1).first()

        if next_lesson:
            user.allowed_courses.add(next_lesson)
            send_message(
                message="<b>✅ Uyga vazifadan muvaffaqiyatli o'tdingiz\nKeyingi darsga o'tishingiz mumkin ➡️</b>",
                chat_id=user.user_id,
                reply_markup=[
                    ['⏭️ Davom etish'],
                ]
            )
        else:
            send_message(
                message="<b>🥳 tabriklayman!\n\nSiz kursni tugatdingiz</b>",
                chat_id=user.user_id,
            )

    # Agar uyga vazifa muvaffaqiyatsiz bo'lsa
    elif is_successful == 'muvaffaqiyatsiz':
        send_message(
            message="<b>❌ Uyga vazifa muvaffaqiyatsiz bo'ladi.\n\nIltimos qayta urinib ko'ring</b>",
            chat_id=user.user_id,
        )
