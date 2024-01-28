from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # better organisation to keep apps' urls sep.
    path('', include('projects.urls'))
]
