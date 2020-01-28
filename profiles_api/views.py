from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of api view features"""
        an_apiview=["Uses HTTP methods as functions","Similar to djangoview"]

        return Response({"message":"Hello","an apiview":an_apiview})



    def post(self,request):
        """Create a hello message with out name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get("name")

            email=serializer.validated_data.get("email")
            message=f"Hello {name} and your email is {email}"

            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({"method":"PATCH"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":"DELETE"})
