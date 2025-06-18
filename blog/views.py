from django.shortcuts import render, get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BlogList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request):
        blogs=Post.objects.all()
        serializer=PostThumbnailSerializer(blogs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PostDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .permissions import IsOwnerOrReadOnly

class BlogDetail(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsOwnerOrReadOnly]
    
    def get_object(self,pk):
        blog=get_object_or_404(Post, pk=pk)
        return blog

    def get(self,request,pk):
        blog=self.get_object(pk)
        serializer=PostDetailSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self,request,pk):
        blog=self.get_object(pk)
        serializer=PostDetailSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        blog=self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)