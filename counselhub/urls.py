from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    
    path('client/', include('clients.urls')),
    path('lawyer/', include('lawyers.urls')),
    
    path("__reload__/", include("django_browser_reload.urls")),
]
