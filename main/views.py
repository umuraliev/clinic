from django.shortcuts import render
from requests import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['speciality', ]
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
