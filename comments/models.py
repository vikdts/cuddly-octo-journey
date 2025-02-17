from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
