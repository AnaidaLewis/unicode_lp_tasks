from django.db import models
from django.contrib.auth.models import AbstractUser

#for token 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length = 100, unique = True, blank = False)
    first_name = models.CharField(max_length = 100, blank = True)
    last_name = models.CharField(max_length = 100, blank = True)
    profile_picture = models.ImageField(default = "Screen_Shot_2021-08-07_at_1.22.31_PM_wVXWw8N.png", null = True, blank= True)
    email = models.EmailField(unique=True, blank = False)
    Created = models.DateTimeField(null = True, blank = False, auto_now_add = True)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)
