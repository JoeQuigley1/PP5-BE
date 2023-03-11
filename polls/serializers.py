from rest_framework import serializers
from polls.models import Poll, Choice


class PollSerializer(serializers.ModelSerializer):
    poll_text = serializers.CharField(max_length=200)
    
    class Meta:
        model = Poll
        fields = [
            'id', 'poll_text', 'created_at'
        ]


class ChoiceSerializer(serializers.ModelSerializer):
    choice_text = serializers.CharField(max_length=200)

    class Meta:
        model = Choice
        fields = [
            'id', 'choice_text', 'created_at'
        ]