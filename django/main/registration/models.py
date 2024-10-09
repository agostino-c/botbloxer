from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have a valid email")
        if not password:
            raise ValueError("No password was provided")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        # user = self.create_user(robloxID, username, **kwargs)
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    class Meta:
        # Verbose Name for Django Admin
        verbose_name = 'Django User'


class RobloxUser(models.Model):
    robloxID = models.CharField(max_length=255, unique=True)
    isBanned = models.BooleanField(default=False)
    banHistory = models.JSONField(default=dict)

    def __str__(self):
        return self.robloxID
    
    class Meta:
        # Verbose Name for Django Admin
        verbose_name = 'Members'