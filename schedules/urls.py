from django.urls import path
from schedules.views import ScheduleListCreate, ScheduleRetrieveUpdateDestroy

urlpatterns = [
    path("", ScheduleListCreate.as_view()),
    path("<int:pk>", ScheduleRetrieveUpdateDestroy.as_view())
]
