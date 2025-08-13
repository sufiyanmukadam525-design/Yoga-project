from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # keep username/email if you want quick access, but they will mirror user.username/email
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254)
    user_type = models.CharField(max_length=1, choices=(
        ("U", "User"),
        ("A", "Admin"),
    ), default="U")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
 


  