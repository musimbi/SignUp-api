from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'Id_number', 'Registration_number', 'Date_Of_Birth', 'Course')