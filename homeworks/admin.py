from django.contrib import admin
from .models import Homework, HomeWorkFiles


class HomeWorkFilesInline(admin.TabularInline):
    model = HomeWorkFiles
    extra = 1  # Number of extra empty forms displayed


@admin.register(Homework)
class HomeworksAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('lesson', 'user', 'send_at', 'is_successful')
    list_filter = ('is_successful', 'send_at')  # Add filters for these fields
    # Enable search on related fields
    search_fields = ('user__name', 'lesson__title')
    inlines = [HomeWorkFilesInline]  # Add the TabularInline
