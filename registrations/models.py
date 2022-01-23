from django.db import models
from schedules.models import Schedule
from students.models import Student
from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="registrations")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="registrations")
    date = models.DateField()
    is_live = models.BooleanField()
    is_recording = models.BooleanField()
    is_paid = models.BooleanField()
