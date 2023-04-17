from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LawyerProfile
# Create your views here.

@login_required(login_url='login')
def LawyerDashboard(request):
    return render(request, 'lawyer/dashboard.html')

@login_required(login_url='login')
def LawyerProfilePage(request, lawyer_id):
    lawyer= LawyerProfile.objects.get(id=lawyer_id)
    context = {'lawyer': lawyer, 'title': lawyer.name}
    return render(request, 'lawyer/profile.html', context)