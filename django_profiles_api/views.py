from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets

# TokenAuthentication for login and 
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# standard Response object to return Response
# when calling the APIView 
from rest_framework.response import Response
# for http status code in returning in post function handler
from rest_framework import status

# import serializers model
from django_profiles_api import serializers
from django_profiles_api import models
from django_profiles_api import permissions


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
    # we can use the same HelloSerializer we've created before
    # serializer knows which field accepts for example creates
    # a field that is used for post when we add the POST method below
    # so those input field(s) come from the serializer
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    # create function for viewsets
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # so those input field(s) come from the serializer :)
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # retrieve a specific obj with retrieve function for viewsets using primary key
    def retrieve(self,request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self,request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # coz of , TokenAuthentication created as tuple not single item
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    # search_fields class variable
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    # when a new obj is creats Django rest frmaework calls perform_create and passes
    # serializer is a model serializer and has save option assigned to it
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        # the save function saves the content of the serializer to an object in the db
        # request object gets passed into to all viewsets everytime a request is made
        # authenticated user
        serializer.save(user_profile=self.request.user)