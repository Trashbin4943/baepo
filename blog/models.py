from django.db import models
from django.conf import settings


class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(default="")
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title