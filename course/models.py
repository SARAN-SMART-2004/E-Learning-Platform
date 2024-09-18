from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, blank=True)
    max_students = models.IntegerField(default=0)
    difficulty_level = models.CharField(max_length=50)
    is_public = models.BooleanField(default=False)
    qa_enabled = models.BooleanField(default=False)
    course_benefits = models.TextField(blank=True)
    target_audience = models.TextField(blank=True)
    course_duration_hours = models.IntegerField(default=0)
    course_duration_minutes = models.IntegerField(default=0)
    materials_included = models.TextField(blank=True)
    certification = models.TextField(blank=True)
    language = models.TextField(blank=True)
    certification_description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    video = models.FileField(upload_to='course_videos/', blank=True)
    image = models.ImageField(upload_to='course_images/', blank=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback from {self.name} on {self.course.title}"