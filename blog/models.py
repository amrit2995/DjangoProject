from django.db import models
from datetime import datetime
# Create your models here.
class blogposts(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 1000)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.title
