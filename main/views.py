from multiprocessing import managers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from main.serializers import DirectionSerializer, DoctorSerializer, SpecialitySerializer
from .models import *

class DoctorPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
