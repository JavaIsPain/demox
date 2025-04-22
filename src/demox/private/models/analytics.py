from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TweetView(models.Model):
    tweet = models.ForeignKey('public.Tweet', on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['tweet', 'viewed_at']),
        ]

    def __str__(self):
        return f"View on Tweet {self.tweet_id} by {self.viewer or 'anonymous'}"
