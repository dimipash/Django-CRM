from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

TEMPLATES_DIR = settings.TEMPLATES_DIR
print("TEMPLATES_DIR", TEMPLATES_DIR)

def dashboard_webpage(request, *args, **kwargs):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('auth/google/login')

    return render(request, 'dashboard.html', {})

    # html = "<h1 style='color: red;'>Hello, World!</h1>"
    # dashboard_html = TEMPLATES_DIR / 'dashboard.html'
    # if not dashboard_html.exists():
    #     return HttpResponse("Dashboard template not found", status=404)
    # dashboard_html_val = dashboard_html.read_text()
    # _html = dashboard_html_val.format(my_value=str(request.user))
    # return HttpResponse(_html)


def about_us_page(request):
    return render(request, 'about.html', {})
