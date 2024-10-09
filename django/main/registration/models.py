from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, robloxID, username, password):
        if not username:
            raise ValueError("User must have a valid username")
        if not robloxID:
            raise ValueError('User must have a valid Roblox User ID')
        
        if not password:
            raise ValueError("No password was provided")
        
        user = self.model(robloxID=robloxID, username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, robloxID, username, password=None, **kwargs):
        kwargs['password'] = password
        user = self.create_user(robloxID, username, **kwargs)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    robloxID = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=125)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'robloxID'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Django User'