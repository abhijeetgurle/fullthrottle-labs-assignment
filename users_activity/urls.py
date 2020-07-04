from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users_and_activity_periods,
         name='get_users_and_activity_periods'),
]
