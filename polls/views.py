from django.shortcuts import render
from rest_framework import generics
from .models import Poll
from .serializers import PollSerializer


class PollView(generics.ListCreateAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
# Create your views here.
