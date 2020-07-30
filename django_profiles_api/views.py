from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.views import ViewSets
# standard Response object to return Response
# when calling the APIView 
from rest_framework.response import Response
# for http status code in returning in post function handler
from rest_framework import status

# import serializers model
from django_profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    # define url endpoint and assign to this view 
    # set serializer, serializer also does validation 
    serializer_class = serializers.HelloSerializer

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

# self.serializer_class is a standard class function comes with APIView
# req obj
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            # pass in a dictionary to the Response
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handle updating an object, return standard obj, REPLACE"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handle apartial updating an object, only UPDATE the provided in the request, choose raw data"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


## VIEW SETS
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})