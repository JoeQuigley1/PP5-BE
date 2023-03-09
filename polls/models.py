from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poll_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.poll_text


class Choice(models.Model):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
