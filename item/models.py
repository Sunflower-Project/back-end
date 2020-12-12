from django.db import models
from django import forms

# Create your models here.

ITEM_CATEGORIES = (
    ('Indoor Furniture'),
    ('Toys'),
    ('Outdoor Furniture')
)

CONDITION_CATEGORIES = (
    ('Great'),
    ('Fair'),
    ('Poor')
)

CLASSIFICATION = (
    ('Recycle'),
    ('Upcycle')
)
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    comment_body = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Item(models.Model):
    name = models.CharField(max_length = 100)
    category = forms.ChoiceField(choices = ITEM_CATEGORIES)
    condition = forms.ChoiceField(choices = CONDITION_CATEGORIES)
    description = models.CharField(max_length=200)
    classification = forms.ChoiceField(choices = CLASSIFICATION)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='items'
    )
