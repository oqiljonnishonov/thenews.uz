from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
import random
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from drf_yasg.utils import swagger_auto_schema

from newsapp.models import (Category , News , Author , User)
from newsapp.serializers import (CategorySerializers , NewsSerializers , AuthorSerializers)



class CategoryAPIView(APIView):
    serializer_class=CategorySerializers
    permission_classes=(AllowAny,)
    @swagger_auto_schema(request_body=CategorySerializers)

    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializers(categories,many=True)
        return Response(data=serializer.data)



    def post(self,request):
        pass





class NewsAPIView(APIView):
    serializer_class=NewsSerializers
    permission_classes=(AllowAny,)
    @swagger_auto_schema(request_body=NewsSerializers)
    
    def get(self,request):
        news=News.objects.all()
        serializer=NewsSerializers(news,many=True)
        return Response(data=serializer.data)


    def post(self, request):
        pass




class AuthorAPIView(APIView):
    serializer_class=AuthorSerializers
    permission_classes=(AllowAny,)
    @swagger_auto_schema(request_body=AuthorSerializers)
    
    def get(self,request):
        authors=Author.objects.all()
        serializer=NewsSerializers(authors,many=True)
        return Response(data=serializer.data)


    def post(self, request):
        pass




