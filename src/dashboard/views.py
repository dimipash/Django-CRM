from django.shortcuts import redirect
from django.http import HttpResponse

def dashboard_webpage(request, *args, **kwargs):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('auth/google/login')
    return HttpResponse("Hello")
