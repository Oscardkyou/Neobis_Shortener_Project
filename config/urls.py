from django.contrib import admin
from django.urls import path, include
from url.views import simple_ui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('url.urls')),  # Include your app's URLs here
    path('', simple_ui)
]