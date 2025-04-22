from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template("public/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def pricing(request):
    template = loader.get_template("public/pricing.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("public/about.html")
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("public/auth/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("public/auth/register.html")
    context = {}
    return HttpResponse(template.render(context, request))
