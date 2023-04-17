from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lawyers.models import LawyerProfile
# Create your views here.

@login_required(login_url='login')
def ClientDashboard(request):
    lawyers = LawyerProfile.objects.all()
    
    context = {'lawyers': lawyers, 'title': 'Dashboard | CounselHub'}
    return render(request, 'clients/dashboard.html', context)
