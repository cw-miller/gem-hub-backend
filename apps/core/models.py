from django.db import models
import uuid

import uuid
from django.db import models

class Profile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    # ✅ THE FIX: primary_key=True
    # This makes 'profile' the actual ID. Django's hidden BigInt 'id' is removed.
    # We remove 'default=uuid.uuid4' because Supabase provides this ID.
    profile = models.UUIDField(primary_key=True, editable=False)
    
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

    class Meta:
        db_table = "profiles"

    def __str__(self):
        # We use self.profile now because self.id no longer exists
        return self.username or str(self.profile)

class Notification(models.Model):
    user = models.ForeignKey(Profile, default=uuid.uuid4, on_delete=models.CASCADE)
    title = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "notifications"

    def __str__(self):
        return f"{self.user_id} - {self.title}"

