from django.db import models

class Notification(models.Model):
    user_id = models.UUIDField(db_index=True, editable=False)  # references profiles.id (UUID) from Supabase
    title = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'notifications'

    def __str__(self):
        return f"{self.user_id} - {self.title}"