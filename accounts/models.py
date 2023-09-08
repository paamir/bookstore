from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)

