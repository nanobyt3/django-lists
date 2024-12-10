from django.db import models
from django.utils import timezone


class Lists(models.Model):
    title = models.CharField(max_length=512)
    details = models.TextField()
    archive = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class List(models.Model):
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    details = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title