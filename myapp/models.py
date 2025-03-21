from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, fullname="Unknown", **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, fullname="Admin", **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, fullname, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Remove the default username field
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)  # Ensure email is unique

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser  # Admins and superusers have all permissions

    def has_module_perms(self, app_label):
        return self.is_superuser
from django.db import models

class HealthData(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    sex = models.CharField(max_length=10)
    height = models.FloatField()
    mood = models.CharField(max_length=20)
    sleep = models.IntegerField()

    def __str__(self):
        return self.name
