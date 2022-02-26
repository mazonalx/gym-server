from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from accounts.models import TimestampedModel

CustomUser = get_user_model()

class UserProfile(TimestampedModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(CustomUser, related_name='profile',on_delete= models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],blank=True, null=True)
    avatar = models.ImageField(upload_to ='profile_images')
    def __str__(self):
        return self.user.username