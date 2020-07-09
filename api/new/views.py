from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
def index(request):
    message = 'server running successfully'
    return Response(data=message, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data='Only for logged in users', status=status.HTTP_200_OK)

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = "success"
            token = Token.objects.get(user=account).key
            data['token'] = token
            data['message'] = "Logged in successfully"
        else:
            data = serializer.errors
        return Response(data)