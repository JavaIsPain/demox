from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    REPORT_REASONS = [
        ('spam', 'Spam or scam'),
        ('abuse', 'Abusive or harmful'),
        ('hate', 'Hate speech'),
        ('nsfw', 'Sexual content'),
        ('other', 'Other'),
    ]

    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('public.Tweet', on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, choices=REPORT_REASONS)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('reporter', 'tweet')

    def __str__(self):
        return f"{self.reporter} reported Tweet {self.tweet_id} ({self.reason})"


class FlaggedTweet(models.Model):
    tweet = models.ForeignKey('public.Tweet', on_delete=models.CASCADE)
    flagged_by_system = models.BooleanField(default=False)
    flagged_by_moderator = models.BooleanField(default=False)
    flagged_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Flagged Tweet {self.tweet_id} (System: {self.flagged_by_system})"
