from django.contrib import admin
from .models.analytics import TweetView
from .models.moderation import FlaggedTweet, Report
from .models.relationships import Follow, Block, Mute

admin.site.register(TweetView)
admin.site.register(FlaggedTweet)
admin.site.register(Report)
admin.site.register(Follow)
admin.site.register(Block)
admin.site.register(Mute)