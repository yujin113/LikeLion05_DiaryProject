from django.db import models
from django.utils import timezone

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    weather = models.CharField(max_length=50, default="")
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]