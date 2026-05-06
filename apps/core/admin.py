from django.contrib import admin
from .models import Notification, Profile


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "title",
        "is_read",
        "time",
    )
    search_fields = ("user_id", "title", "message")
    list_filter = ("is_read", "time")
    ordering = ("-time",)
    readonly_fields = ("time",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "username",
        "phone",
        "created_at",
        "updated_at",
    )

    search_fields = ("profile", "username", "phone", "description")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    readonly_fields = ("profile", "created_at", "updated_at")
