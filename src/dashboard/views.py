from django.conf import settings
from django.shortcuts import redirect, render

TEMPLATES_DIR = settings.TEMPLATES_DIR
print("TEMPLATES_DIR", TEMPLATES_DIR)

def dashboard_webpage(request, *args, **kwargs):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('auth/google/login')

    return render(request, 'dashboard/main.html', {})

def about_us_page(request):
    return render(request, 'about.html', {})
