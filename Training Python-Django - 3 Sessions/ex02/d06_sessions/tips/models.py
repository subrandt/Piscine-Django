from django.db import models
from django.conf import settings

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
