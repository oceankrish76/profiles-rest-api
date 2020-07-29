from django.shortcuts import render

from rest_framework.views import APIView
# standard Response object to return Response
# when calling the APIView 
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    # define url endpoint and assign to this view 

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # an_apiview list
        an_apiview = [
            'Uses HTTP methods as funciton (get, post, patch, put, delete)',
            'Is similar to a traditional Django View but intended to use for APIS',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
        ]
        # return list or dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

