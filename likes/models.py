from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
