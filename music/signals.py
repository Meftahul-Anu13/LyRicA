from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from .models import User

@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    if isinstance(user, User):  # Ensure it's your custom user
        user.last_login = now()
        user.save()
