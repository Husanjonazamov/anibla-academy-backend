from rest_framework import serializers
from .models import BotUser
from lessons.serializers import LessonListSerializer
from django.utils.timezone import now


class UserSerializers(serializers.ModelSerializer):
    allowed_courses = LessonListSerializer(
        many=True, read_only=True)  # ManyToMany maydon uchun serializer
    purchase_time = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S', read_only=True)  # Vaqt formatlash

    class Meta:
        model = BotUser
        fields = ('user_id', 'name', 'phone', 'is_purchased',
                  'purchase_time', 'allowed_courses')  # Maydonlar

    def update(self, instance, validated_data):
        # Foydalanuvchini yangilash
        is_purchased = validated_data.get(
            'is_purchased', instance.is_purchased)

        # Agar `is_purchased` True bo'lsa va yangi holat bo'lsa
        if is_purchased and not instance.purchase_time:
            instance.purchase_time = now()  # Sotib olish vaqtini o'rnatish
            instance.is_purchased = is_purchased
            instance.save()
            # `allowed_courses`ni yangilash
            from botusers.services import update_allowed_courses
            update_allowed_courses(instance)

        # Oddiy yangilash
        return super().update(instance, validated_data)
