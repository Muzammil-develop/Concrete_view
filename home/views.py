from django.shortcuts import render
from home.models import Outlet
from home.api_file.serializer import OutletSerializer
from rest_framework import generics

# Create your views here.

class Outlet_view (generics.ListCreateAPIView):
    queryset = Outlet.objects.all ()
    serializer_class = OutletSerializer

class Outlet_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outlet.objects.all ()
    serializer_class = OutletSerializer
