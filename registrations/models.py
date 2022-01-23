from django.db import models
from schedules.models import Schedule
from students.models import Student

class Registration(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="registrations")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="registrations")
    date = models.DateField()
    is_live = models.BooleanField()
    is_recording = models.BooleanField()
    is_paid = models.BooleanField()
