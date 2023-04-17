from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginUser, name='login'),
    path('signup/', views.SignUpUser, name='signup'),
    path('profile/', views.Profile, name='profile'),
    path('logout/', views.LogoutUser, name='logout')
]
