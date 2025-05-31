from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse


@api_view(['GET'])
@permission_classes([AllowAny])
def show_login(request):
    return render(request, 'auth/login.html')


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user, created = User.objects.get_or_create(username='default_user')
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return JsonResponse({'access_token': access_token})


@api_view(['GET'])
@permission_classes([AllowAny])
def protected(request):
    return render(request, 'auth/protected.html')
