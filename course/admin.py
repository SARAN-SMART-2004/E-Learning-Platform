from django.contrib import admin
from .models import Course, Enrollment,Feedback

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Feedback)
