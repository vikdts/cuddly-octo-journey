from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from ads.models import Ad

# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE, default=1
    )
    ad = models.ForeignKey(
        Ad, related_name='likes', on_delete=models.CASCADE, default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post', 'ad']

    def __str__(self):
        liked = self.get_liked()
        return f'{self.owner} {liked}'

    def get_liked(self):
        if self.post:
            return self.post
        elif self.ad:
            return self.ad
        return None
