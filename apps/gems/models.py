from django.db import models
from apps.core.models import Profile
import uuid


class GemListing(models.Model):
    owner = models.ForeignKey(Profile, default=uuid.uuid4, on_delete=models.CASCADE)
    name = models.TextField()
    carat = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    seller_phone = models.TextField(null=True, blank=True)
    status = models.TextField(default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gem_listings"

    def __str__(self):
        return self.name
