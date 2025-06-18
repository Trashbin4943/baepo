from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserList(APIView):
    def get(self,request):
        members=CustomUser.objects.all()
        serializer=UserInfoSerializer(members,many=True)
        return Response(serializer.data)
