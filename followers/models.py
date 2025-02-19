from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follower(models.Model):
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )