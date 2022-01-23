from django.db import models


class Schedule(models.Model):
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    type = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    day = models.CharField(max_length=1, choices=DAY_CHOICES)
    time = models.TimeField()
    length = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

