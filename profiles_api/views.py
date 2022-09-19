from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


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
        