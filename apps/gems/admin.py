from django.contrib import admin
from .models import GemListing


@admin.register(GemListing)
class GemListingAdmin(admin.ModelAdmin):
    list_display = (
        "gem_id",
        "name",
        "owner_id",
        "carat",
        "price",
        "location",
        "status",
        "created_at",
    )
    search_fields = ("name", "owner_id", "location", "status")
    list_filter = ("status", "created_at", "location")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
