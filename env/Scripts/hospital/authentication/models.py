"""from django.db import models


# Create your models here.

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    choice = (("Doctor", "Doctor"), ("ServiceReceptionist", "ServiceReceptionist"), ("WelcomeReceptionist", "WelcomeReceptionist"), ("PaymentBox", "PaymentBox"))
    job = models.CharField(max_length = 200, choices = choice, null = True, blank = True)
  """