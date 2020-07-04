from django.db import models
from timezone_field import TimeZoneField


class User(models.Model):
    """
        Model class to represent user data
    """
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=200)
    timezone = TimeZoneField()

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    """
        Model class to represent start and end time of activities by a user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)
