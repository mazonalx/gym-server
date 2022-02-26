from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .managers import CustomUserManager

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ('-created_at', '-updated_at')
        
class CustomUser(AbstractBaseUser,PermissionsMixin,TimestampedModel):
    email = models.EmailField(_('email address'),max_length=50,unique=True)
    username = models.CharField(_('username'),max_length=150,unique=True)
    first_name = models.CharField(_('first name'),max_length=30)
    last_name = models.CharField(_('last name'),max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email