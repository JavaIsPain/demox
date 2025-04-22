from django.contrib import admin
from .models import Profile, Tweet, Like, Notification, Follow

admin.site.register(Profile)
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(Follow)
