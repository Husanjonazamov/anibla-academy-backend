from django.contrib import admin
from .models import BotUser
from django.utils.html import format_html

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ('user_id', 'name', 'phone', 'is_purchased',
                    'purchase_time', 'allowed_courses_display')

    # Fields displayed in the form view
    fields = ('user_id', 'name', 'phone', 'is_purchased',
              'purchase_time', 'allowed_courses')

    # Fields that should be search-enabled in the list view
    search_fields = ('user_id', 'name', 'phone')

    # Add filter functionality in the list view
    list_filter = ('is_purchased',)

    # Add the ability to display the allowed courses in a human-readable format in the list view
    def allowed_courses_display(self, obj):
        return format_html(', '.join([lesson.title for lesson in obj.allowed_courses.all()]))
    allowed_courses_display.short_description = 'Allowed Courses'

    # Readonly fields
    readonly_fields = ('purchase_time',)

    # You can add extra customization if needed
