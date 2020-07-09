from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone_number = models.CharField(null=True, max_length=100)
    Id_number = models.CharField(max_length=100, unique=True)
    Registration_number = models.CharField(max_length=100, unique=True)
    Date_Of_Birth = models.DateTimeField(auto_now_add=True)
    Course = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['username', 'phone_number', 'first_name', 'last_name', 'Id_number', 'Registration_number', 'Date_Of_Birth', 'Course']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

