# from django.contrib import admin
# from .models import Lesson, Video, File, Photo, Voice


# class VoiceInline(admin.TabularInline):
#     model = Voice
#     extra = 1  # Display one empty row for adding new entries by default
#     fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


# class PhotoInline(admin.TabularInline):
#     model = Photo
#     extra = 1  # Display one empty row for adding new entries by default
#     fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


# class VideoInline(admin.TabularInline):
#     model = Video
#     extra = 1  # Display one empty row for adding new entries by default
#     fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


# class FileInline(admin.TabularInline):
#     model = File
#     extra = 1
#     fk_name = 'lesson'


# @admin.register(Lesson)
# class LessonsAdmin(admin.ModelAdmin):
#     # Fields shown in the list view
#     list_display = ('title', 'description', 'date', 'start_date',
#                     'get_video_count', 'get_photo_count')
#     list_filter = ('date', 'start_date')  # Filter by date and start date
#     # Enable search by title and description
#     search_fields = ('title', 'description')
#     # Default ordering by start date (newest first)
#     ordering = ('-start_date',)
#     inlines = [VideoInline, FileInline, PhotoInline, VoiceInline]

#     # Method to show the count of associated videos in the list view
#     def get_video_count(self, obj):
#         return obj.video_set.count()
#     get_video_count.short_description = 'Video Count'

#     # Method to show the count of associated photos in the list view
#     def get_photo_count(self, obj):
#         return obj.photo_set.count()
#     get_photo_count.short_description = 'Photo Count'

#     # Customizing the layout of the form when editing
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'date', 'start_date')
#         }),
#         ('Media Files', {
#             'classes': ('collapse',),
#             'fields': ('video', 'photo', 'file', 'voice')
#         }),
#     )

#     # Add a custom header for the list view
#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['title'] = "Manage Lessons"
#         return super().changelist_view(request, extra_context=extra_context)


from django.contrib import admin
from .models import Lesson, Video, File, Photo,  Voice


class VoiceInline(admin.TabularInline):
    model = Voice
    extra = 1  # Display one empty row for adding new entries by default
    fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Display one empty row for adding new entries by default
    fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1  # Display one empty row for adding new entries by default
    fk_name = 'lesson'  # Specifies the ForeignKey linking to Lesson


class FileInline(admin.TabularInline):
    model = File
    extra = 1
    fk_name = 'lesson'


@admin.register(Lesson)
class LessonsAdmin(admin.ModelAdmin):
    # Fields shown in the list view
    list_display = ('title', 'description', 'date', 'start_date')
    inlines = [VideoInline, FileInline, PhotoInline,
               VoiceInline]  # Add inlines for Videos and Files
