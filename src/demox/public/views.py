from django.http import HttpResponse

def home(request):
    return HttpResponse("Public Home Page")

def pricing(request):
    return HttpResponse("Pricing Page")

def about(request):
    return HttpResponse("About Us")

def login(request):
    return HttpResponse("Login Page")

def register(request):
    return HttpResponse("Register Page")
