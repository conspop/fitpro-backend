from django.urls import path
from .views import RegistrationListCreate, RegistrationRetrieveUpdateDestroy

urlpatterns = [
    path("", RegistrationListCreate.as_view()),
    path("<int:pk>", RegistrationRetrieveUpdateDestroy.as_view())
]
