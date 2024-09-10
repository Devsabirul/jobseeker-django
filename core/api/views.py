from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class Startproject(APIView):
    def get(self,request):
        return Response({"msg":"Welcome to the project."},status=status.HTTP_200_OK)
