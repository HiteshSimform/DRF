from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

