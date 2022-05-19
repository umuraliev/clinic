from multiprocessing import managers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main.serializers import DirectionSerializer, DoctorSerializer, SpecialitySerializer
from .models import *



class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
