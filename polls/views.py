from django.shortcuts import render
from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer


class PollListView(generics.ListCreateAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoiceView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class PollDetail(generics.RetrieveDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
# Create your views here.
