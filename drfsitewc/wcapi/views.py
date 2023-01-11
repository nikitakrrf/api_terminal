from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wcapi
from .serializers import WcapiSerializer

class WcapiAPIViewStatistics(APIView):
    def post(self,request):
        return Response({'user': 'pass'})

class WcapiAPIViewSettings(APIView):
    def post(self,request):
        return Response({'user': 'pass'})

class WcapiAPIViewHistory(APIView):
    def post(self,request):
        return Response({'user': 'pass'})

class WcapiAPIViewQR(APIView):
    def post(self,request):
        return Response({'user': 'pass'})

class WcapiAPIViewCheckOrder(APIView):
    def post(self,request):
        return Response({'user': 'pass'})

class WcapiAPIViewOrder(APIView):
    def post(self,request):
        return Response({'user': 'pass'})




