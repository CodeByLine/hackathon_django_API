### views.py

from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# from django.contrib.auth import get_user_model


# class UserSerializer(serializers.ModelSerializer): #needed for restframework
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'password')
#         extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

#     def create(self, validated_data):
#         return get_user_model().objects.create_user(**validated_data)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model.objects.all()
#     serializer_class = UserSerializer

    