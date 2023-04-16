from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.LawyerDashboard, name='lawyer-dashboard'),
]
