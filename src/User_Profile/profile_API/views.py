from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Hello_APIView(APIView):
    """ Test API View """

    def get(self,request,format=None):
        """ Return list of feature offered by API View """
        api_view=[
        'Uses HTTP methods as function(get,post,delete,put,patch)',
        'It is similar to traditional django views',
        'Gives you the most control over logics',
        'It mapped manually to URLs'
        ]
        return Response({'message':'Hello Rishabh','api_view':api_view})
