from django.db import models
from django.contrib.auth.models import User

class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='tip_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='tip_downvotes', blank=True)

    def __str__(self):
        return self.content[:50]