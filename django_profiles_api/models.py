from django.db import models

# standard classes to use in order to override
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager): # BaseUserManager as a parent class 
    """Manager for user profiles"""

    # self arg for class function
    # self is automatically passed in for any class function
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            # raise a value error exception
            raise ValueError("User must have an email address")

        # normalize the email address lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db) # standard django procedure to save obj in django

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        # coz of automatically passing self, we don't need to pass self while calling
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # model managers for the user model
    # UserProfileManager to be created
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

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


class ProfileFeedItem(models.Model):
    """Profile status update"""
    # Relationship with UserProfile model
    # UserProfile model is in settings.py file as AUTH_USER_MODEL
    # If user is deleted, all the feed from that use are also deleted
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    # convert model instance to str for TokenAuthentication

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
