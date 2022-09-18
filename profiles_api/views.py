from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(Self, request , format=None):
        """return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similiar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]
        return Response({'messgae':'Hello!','an_apiview': an_apiview})