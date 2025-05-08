from email.policy import default
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser, BaseUserManager



def generate_id():
    return uuid4().hex


# Create your models here.
class FoodMenu(models.Model):
    id = models.CharField(max_length=255, default=generate_id, primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=False)
    time = models.DateTimeField(auto_now=True)
    image = models.URLField(blank=True, null=True)
    price = models.FloatField(null=False)

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         upload_result = uploader.upload(self.image)
    #         self.image=upload_result['secure_url']
    #     super().save(*args, **kwargs)

class Add_ons(models.Model):
    id = models.CharField(max_length=255, default = generate_id, primary_key = True, unique = True)
    name = models.CharField(max_length=50, null=False)
    food_menu = models.ForeignKey(FoodMenu, on_delete=models.CASCADE, blank=True)

class Food_rider(models.Model):
    id = models.CharField(max_length=255, default=generate_id, primary_key=True, unique=True)
    name = models.CharField(max_length=255, null=False)


class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **kwargs):
        if not email:
            raise ValueError('Email field is Required')
        if not password:
            raise ValueError('Password Field is Required')
        if not username:
            raise ValueError('username field is Required')
        print(username, 'username')

        user = self.model(email = self.normalize_email(email), username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('is_staff value is required')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('is_superuser is requried')

        return self.create_user(email = email, username=username, password=password, **kwargs)

class User(AbstractUser):
    USERNAME_FIELD = 'username'
    id = models.CharField(max_length=255, default=generate_id, primary_key=True, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False)
    username = models.CharField(max_length = 20, unique = True, null = False)

    REQUIRED_FIELDS= ['email']
    objects=UserManager()



