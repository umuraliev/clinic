from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Direction
from .helpers import SpecialityFilter

from main.serializers import DoctorSerializer, ReviewSerializer, SpecialitySerializer
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
        queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    
class SpecialityListView(ListAPIView):
    """List of specialities"""
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['direction', ]

    # def get(self, request):
    #     specialities = Speciality.objects.all()
    #     serializer = SpecialitySerializer(specialities, many=True)
    #     return Response(serializer.data)

    
    # @action(detail=False, methods=['get'])
    # def direction(self, request):
    #     q = request.query_params.get('q')
    #     queryset = self.get_queryset()
    #     queryset = queryset.filter(Q(speciality__contains=q))
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,  ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}
