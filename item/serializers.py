from rest_framework import serializers
from . import models
from .models import Item, Comment

class ItemSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(
        source = 'item.name',
        read_only = True
    )
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'condition', 'description', 'classification', 'comment', 'item')

class CommentSerializer(serializers.ModelSerializer):
    comment = ItemSerializer(
        many = True,
        read_only = True
    )

    class Meta:
        model: Comment
        fields = ('id', 'user_name', 'comment_body', 'comment_name')
