from django.shortcuts import render
from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Poll
from .serializers import PollSerializer


class PollListView(generics.ListCreateAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
# Create your views here.
