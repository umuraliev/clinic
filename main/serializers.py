
from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Doctor
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True, context=self.context).data
        representation['likes']=instance.likes.all().count()
        return representation


class SpecialitySerializer(serializers.ModelSerializer):
    direction = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Speciality
        fields = ('title', 'direction' )


class ReviewSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Review.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
