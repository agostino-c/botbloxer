from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, robloxID, username):
        if not username: raise ValueError("User must have a valid username")
        if not robloxID:
            # Add some sort of handshake check to see if this is valid?
            raise ValueError('User must have a valid Roblox User ID')
        
        user = self.model(robloxID=robloxID, username=username)
        # user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, robloxID, username, password):
        user = self.create_user(robloxID, username, password)
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
    



"""



    

class VerifiedDiscords(models.Model):
    discordID = models.CharField(max_length=150)
    state = models.CharField(max_length=255)
    taken = models.BooleanField(default=False)

"""