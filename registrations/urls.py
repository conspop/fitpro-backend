from django.urls import path
from .views import RegisterListCreate, RegistrationRetrieveUpdateDestroy

urlpatterns = [
    path("", RegisterListCreate.as_view()),
    path("<int:pk>", RegistrationRetrieveUpdateDestroy.as_view())
]
