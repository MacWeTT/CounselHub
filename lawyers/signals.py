from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .models import LawyerProfile

@receiver(post_save, sender=Profile)
def create_lawyer_profile(sender, instance, created, **kwargs):
    if created and instance.profession == '1':
        LawyerProfile.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def update_lawyer_type(sender, instance, **kwargs):
    if instance.profession == '1':
        instance.lawyerprofile.lawyer_type = instance.occupation
        instance.lawyerprofile.save()