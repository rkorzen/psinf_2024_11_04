from django.shortcuts import render
from rest_framework import viewsets
from .models import Szkolenie
from .serializers import SzkolenieSerializer


# Create your views here.




class SzkolenieViewSet(viewsets.ModelViewSet):
    queryset = Szkolenie.objects.all()
    serializer_class = SzkolenieSerializer