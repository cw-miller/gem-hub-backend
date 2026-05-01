from django.db import models
from apps.core.models import Profile
import uuid

class Job(models.Model):
    employer = models.ForeignKey(Profile, default=uuid.uuid4, on_delete=models.CASCADE)
    title = models.TextField()
    company_info = models.TextField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    logo_color = models.IntegerField(null=True, blank=True)
    status = models.TextField(default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "jobs"

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, default=uuid.uuid4, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone = models.TextField(null=True, blank=True)
    expected_salary = models.FloatField(null=True, blank=True)
    cv_url = models.TextField(null=True, blank=True)
    status = models.TextField(default="pending")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "applications"

    def __str__(self):
        return f"{self.applicant_id} - {self.job.title}"
