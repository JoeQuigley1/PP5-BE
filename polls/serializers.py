from rest_framework import serializers
from polls.models import Poll


class PollSerializer(serializers.ModelSerializer):
    poll_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        model = Poll
        fields = [
            'id', 'poll_text', 'created_at'
        ]