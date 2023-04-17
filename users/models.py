from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

Professions = (
    ("1", "Lawyer"),
    ("2", "Client"),
)

def validate_aadhaar_number(value):
    if not value.isdigit():
        raise ValidationError('Aadhaar number should contain only digits.')
    if len(value) != 12:
        raise ValidationError('Aadhaar number should be exactly 12 digits.')

class Profile(models.Model):
    is_complete = models.BooleanField(default=False)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=10, choices=Professions, default="2", null=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=20, null=True, blank=True)
    aadhar = models.CharField(max_length=12, null=True, blank=True, validators=[validate_aadhaar_number])
    
    def __str__(self):
        return self.user.email

