from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count



class CustomUser(AbstractUser):
    # 'username', 'email', 'first_name', 'last_name', 'password' fields are already part of AbstractUser
