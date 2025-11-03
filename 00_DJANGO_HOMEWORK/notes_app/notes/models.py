from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


def default_note_title():
    return f"New note ({datetime.datetime.now()})"

class Note(models.Model):

    title = models.CharField(max_length=100, default = default_note_title)
    text = models.TextField()
    reminder = models.DateTimeField(default=datetime.datetime.now)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='notes', on_delete=models.CASCADE)

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




