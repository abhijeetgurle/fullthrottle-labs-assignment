from django.core.management.base import BaseCommand
from users_activity.models import User, ActivityPeriod
from .data import data


class Command(BaseCommand):
    def _create_users(self):
        for i in range(len(data)):
            user = User(
                id=data[i]['id'], real_name=data[i]['real_name'], timezone=data[i]['tz'])
            user.save()

    def _create_activity_periods(self):
        for i in range(len(data)):
            for j in range(len(data[i]['activity_periods'])):
                activity_data = data[i]['activity_periods'][j]
                activity_period = ActivityPeriod(
                    user=User(id=data[i]['id']), start_time=activity_data['start_time'], end_time=activity_data['end_time'])
                activity_period.save()

    def handle(self, *args, **options):
        self._create_users()
        self._create_activity_periods()
