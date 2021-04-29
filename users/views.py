#users/views.py

from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model
from .models import User
from .permissions import ObjectPermission

#needed for restframework
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


    def create(self, validated_data):
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        # raise PermissionDenied()
        pass