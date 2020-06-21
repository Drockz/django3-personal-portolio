from django.db import models
from datetime import datetime, date

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
