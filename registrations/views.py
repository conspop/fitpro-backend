from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer

from rest_framework import generics

class RegistrationListCreate(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.registrations.all()

class RegistrationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.registrations.all()