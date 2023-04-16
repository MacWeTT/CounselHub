from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def ClientDashboard(request):
    return render(request, 'clients/dashboard.html')