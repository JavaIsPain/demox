from django.urls import path
from . import views

auth_urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
]

urlpatterns = [
    path("", views.home, name="home"),
    path("pricing", views.pricing, name="pricing"),
    path("about", views.about, name="about"),
    path("auth/", (auth_urlpatterns, 'auth', 'auth')),
]
