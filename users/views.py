from http.client import SERVICE_UNAVAILABLE
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import *


class UserList(generics.ListAPIView):
    
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer