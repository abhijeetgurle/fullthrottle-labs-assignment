from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import User, ActivityPeriod


# Create your views here.
def get_users_and_activity_periods(request):
    """
    Returns the json object containing users and their activity periods

        Parameters:
            request: A http request from the client

        Returns:
            json_response: Containig data of users and their activity periods or an error message
    """

    try:
        members = []
        users = User.objects.all()
        for user in users:
            member_data = {"id": user.id,
                           "real_name": user.real_name, "tz": str(user.timezone)}

            activity_periods = []
            member_activities = ActivityPeriod.objects.filter(user=user)
            for activity in member_activities:
                start_time = change_date_time_format(
                    activity.start_time)
                end_time = change_date_time_format(activity.end_time)
                activity_period = {
                    "start_time": start_time, "end_time": end_time}
                activity_periods.append(activity_period)

            member_data["activity_periods"] = activity_periods
            members.append(member_data)

        return JsonResponse({"ok": True, "members": members})
    except Exception as e:
        return JsonResponse({"ok": False, "members": None, "message": "Something went wrong on server"}, status=500)


def change_date_time_format(datetime_object):
    """
        Returns the date and time in new format

        Parameters:
            datetime_object: A datetime object

        Returns:
            datetime_string: A new datetime string in new format
    """
    time = str(datetime_object.replace(tzinfo=None))
    old_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return old_time.strftime("%b %d %Y %I:%M %p")
