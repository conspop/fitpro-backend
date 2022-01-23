from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDestroy

urlpatterns = [
    path("", StudentListCreate.as_view()),
    path("<int:pk>", StudentRetrieveUpdateDestroy.as_view())
]
