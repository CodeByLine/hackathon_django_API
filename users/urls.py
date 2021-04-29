#users/urls.py

from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from .views import (
    UserViewSet, #SubmissionsViewSet, CustomAuthToken, UserProfileView
)


# Django REST Framework router
router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]