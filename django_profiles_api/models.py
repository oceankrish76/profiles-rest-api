from django.db import models

# standard classes to use in order to override
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # model managers for the user model
    # UserProfileManager to be created
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    # functions to interact
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    # specify string representation of our model
    def __str__(self):
        """Return string representation of our user"""
        return self.email
