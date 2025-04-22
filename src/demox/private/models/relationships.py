from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.follower} → {self.following}"


class Block(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocking_set')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_by_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocker', 'blocked')

    def __str__(self):
        return f"{self.blocker} blocked {self.blocked}"


class Mute(models.Model):
    muter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='muting_set')
    muted = models.ForeignKey(User, on_delete=models.CASCADE, related_name='muted_by_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('muter', 'muted')

    def __str__(self):
        return f"{self.muter} muted {self.muted}"
