from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .helpers import send_confirmation_email
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView


User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            code = serializer.validated_data['activation_code']
            user = get_object_or_404(User, activation_code=code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'User Succesfully activated'})

# class LostPassView(APIView):
#     def post(self, request):
#         serializer = LostPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             send_confirmation_email(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)

# class CreateNewPassView(APIView):
#     def post(self, request):
#         serializer = CreateNewPasswordSerializer(data=request.data)
        


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )