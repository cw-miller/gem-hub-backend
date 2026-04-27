from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'title',
        'is_read',
        'time',
    )
    search_fields = ('user_id', 'title', 'message')
    list_filter = ('is_read', 'time')
    ordering = ('-time',)
    readonly_fields = ('time',)