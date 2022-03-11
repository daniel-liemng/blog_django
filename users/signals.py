from django.db.models.signals import post_save
# User is called the center: where to send the signal
from django.contrib.auth.models import User
# Receiver is a function that gets the signals and perform tasks
from django.dispatch import receiver
from .models import Profile

# User profile is created for each new user
# if the user is saved, send the signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()
