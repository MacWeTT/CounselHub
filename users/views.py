from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm
# Create your views here.

def home(request):
    context = {'title': 'Home | CounselHub'}
    return render(request, 'home.html', context)

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'users/login.html', {'title': 'Login | CounselHub'})

def SignUpUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request ,user)
            messages.success(request, 'Account created successfully.')
            return redirect('profile')
        else:
            print(form.errors)
            messages.error(request,"An error occured. Check if details are correct and password is valid.")
    else:    
        form = UserRegisterForm()
    
    context = {'title': 'Signup | CounselHub','form': form}
        
    return render(request, 'users/signup.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            request.user.profile.is_complete = True
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully.')
            if request.user.profile.profession == '1':
                return redirect('lawyer-dashboard')
            else:
                return redirect('client-dashboard')
        else:
            messages.error(request, 'Error updating profile. Check if everything is correct.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        
    context = {'u_form': u_form,'p_form': p_form, 'title': 'Complete Profile | CounselHub'}
            
    return render(request, 'users/profile.html', context)