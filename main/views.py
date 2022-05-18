from multiprocessing import managers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main.serializers import DoctorSerializer
from .models import Doctor



class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
