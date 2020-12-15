from rest_framework import serializers
from . import models
from .models import Item, Comment

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

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices = ITEM_CATEGORIES)
    condition = serializers.ChoiceField(choices = CONDITION_CATEGORIES)
    classification = serializers.ChoiceField(choices = CLASSIFICATION)
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'condition', 'description', 'classification', 'image')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user_name', 'comment_body', 'comment_name')
