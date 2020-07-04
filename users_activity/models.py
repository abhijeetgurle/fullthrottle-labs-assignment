from django.db import models
from timezone_field import TimeZoneField


class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=200)
    timezone = TimeZoneField()

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)
