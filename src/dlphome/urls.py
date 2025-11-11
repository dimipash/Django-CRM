
from django.contrib import admin
from django.urls import path, include

from contacts.views import contacts_list_view
from dashboard.views import dashboard_webpage, about_us_page

urlpatterns = [
    path('', dashboard_webpage),
    path('contacts/', contacts_list_view),
    path('dashboard/', dashboard_webpage),
    path('about/', about_us_page),
    path('admin/', admin.site.urls),
    path("auth/", include("django_googler.urls.default")),
]
