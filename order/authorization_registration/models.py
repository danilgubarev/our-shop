from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class BuyerManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Buyer(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True, default='example@example.com')
    password = models.CharField(max_length=100, unique=True, default='12345678')
    objects = BuyerManager()
    USERNAME_FIELD = 'username'