from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.ClientDashboard, name='client-dashboard'),
]
