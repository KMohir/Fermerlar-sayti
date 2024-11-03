from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError("Users must have a login")
        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        user = self.create_user(login, password)
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    login = models.CharField(max_length=255, unique=True)
    is_superadmin = models.BooleanField(default=False)
    token = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'login'

    objects = UserManager()

    def __str__(self):
        return self.login