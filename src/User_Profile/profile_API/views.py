from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class Hello_APIView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ Return list of feature offered by API View """
        api_view=[
        'Uses HTTP methods as function(get,post,delete,put,patch)',
        'It is similar to traditional django views',
        'Gives you the most control over logics',
        'It mapped manually to URLs'
        ]
        return Response({'message':'Hello Rishabh','api_view':api_view})

    def post(self,request):
        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'put'})

    def delete(self,request):
        return Response({'method':'delete'})



class HelloViewsets(viewsets.ViewSet):
    def list(self,request):
        api_view=[
        'DOest not uses HTTP methods as function(get,post,delete,put,patch)',
        'It is similar to traditional django views',
        'Best to use when intracting with database',
        'Automatically map to urls using router class'
        ]
        return Response({'message':'Hello Rishabh','api_view':api_view})
