from django.db import models
from django import forms

# Create your models here.


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    comment_body = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Item(models.Model):
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length=100, default='')
    condition = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200)
    classification = models.CharField(max_length=100, default='')
    item_type = models.CharField(max_length=100, default='')
    image = models.ImageField(
        upload_to='media/', default='media/NoImage.jpg')
