from django.db import models
from django.core.exceptions import ValidationError
from users.models import Profile
# Create your models here.

def validate_profile_complete(user):
    if not user.profile.is_complete or user.profile.profession != '1':
        raise ValidationError('You must complete your profile as a lawyer before creating a Lawyer Profile.')

class LawyerProfile(models.Model):
    name = models.CharField(max_length=100, default='Lawyer')
    lawyer_type = models.CharField(max_length=100, default='Corporate Lawyer')
    description = models.CharField(max_length=200, null=True, blank=True)
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def clean(self) -> None:
        validate_profile_complete(self.profile.user)
        return super().clean()