from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        print(request.auth.key)
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def blog_details(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error':'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response({'message':'Blog deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)