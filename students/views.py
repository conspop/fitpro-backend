from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer

from rest_framework import generics

class StudentListCreate(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.students.all()

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.students.all()