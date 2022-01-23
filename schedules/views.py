from rest_framework.permissions import IsAuthenticated
from .serializers import ScheduleSerializer

from rest_framework import generics

class ScheduleListCreate(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.schedules.all()

class ScheduleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.schedules.all()