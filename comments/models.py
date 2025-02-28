from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from ads.models import Ad

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    def clean(self):
        if not self.post and not self.ad:
            raise ValidationError("post or ad")
        if self.post and self.ad:
            raise ValidationError("post or ad")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)