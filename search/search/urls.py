from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', admin.site.urls),
    path('profiles/', admin.site.urls),
]
