from django.urls import path
from . import views

urlpatterns = [
    path("feed", views.feed, name="feed"),
    path("settings", views.settings, name="settings"),
    path("settings/<uuid:user_uuid>", views.settings, name="user_settings"),
    path("profile/<slug:account_identifier>", views.profile, name="public_profile"),
    path("profile/<uuid:account_identifier>", views.profile, name="private_profile"),
]
