from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer

    def get(Self, request , format=None):
        """return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similiar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]
        return Response({'messgae':'Hello!','an_apiview': an_apiview})


    def post (self,request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        return Response(serializer.errors,  status= status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):      #pk stands for primary key
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk= None):   #pk stand for primary key
        """handle a partical update of an object"""  #only update the field where data is provided
        return Response({"method":"patch"})

    def delete(self, request , pk =None):  #pk stands for primary
        '''delete am object'''
        return Response({"method":'Delete'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API Viewset'''
    serializer_class= serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''
        a_viewset = [
            'Users actions (list, create, retrieve, update, partical_update',
            "automatically maps to URL using Routers",
            'Proviedes more functionality with less code',
        ]

        return  Response ({"message":'Hello',"a_viewset":a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'Message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self,request, pk =None):
        """handle gettingb an object by  its ID"""
        return Response({'http_method':'GET'})

    def update(self,request, pk=None):
        """Handle updatting an object"""
        return Response({'Http_method':"put"})

    def partical_update(self,request, pk = None):
        '''Handle updatting party of an object'''
        return Response({'http_method':'patch'})

    def destroy(self,request, pk=None):
        '''handle removing an object'''
        return Response ({'ghttp_method':'delete'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating  profiles"""

    serializer_class =serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends= (filters.SearchFilter,)
    search_fields =('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and  updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class =serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )


    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)