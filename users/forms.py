from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profession', 'address', 'occupation', 'aadhar']
