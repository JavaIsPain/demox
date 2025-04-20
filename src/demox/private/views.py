from django.http import HttpResponse

def feed(request):
    return HttpResponse("Feed")

def settings(request, user_uuid=None):
    return HttpResponse(f"Settings Page {user_uuid or ''}")

def profile(request, account_identifier):
    return HttpResponse(f"Profile Page: {account_identifier}")
