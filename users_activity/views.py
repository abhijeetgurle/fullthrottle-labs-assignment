from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import User, ActivityPeriod


# Create your views here.
def get_users_activity_periods(request):
    members = []
    users = User.objects.all()
    for user in users:
        member_data = {"id": user.id,
                       "real_name": user.real_name, "tz": str(user.timezone)}

        activity_periods = []
        member_activities = ActivityPeriod.objects.filter(user=user)
        for activity in member_activities:
            start_time = convertTimeFormat(activity.start_time)
            end_time = convertTimeFormat(activity.end_time)
            activity_period = {
                "start_time": start_time, "end_time": end_time}
            activity_periods.append(activity_period)

        member_data["activity_periods"] = activity_periods
        members.append(member_data)

    return JsonResponse({"ok": True, "members": members})


def convertTimeFormat(datetime_object):
    time = str(datetime_object.replace(tzinfo=None))
    old_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return old_time.strftime("%b %d %Y %I:%M %p")
