from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.LawyerDashboard, name='lawyer-dashboard'),
    path('lawyer/<int:lawyer_id>', views.LawyerProfilePage, name='lawyer-profile')
]
