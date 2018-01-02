from rest_framework import serializers
from channels.models import Category, Channel


class CategorySerializer(serializers.ModelSerializer):
    '''
        This serializer is used to represent a category in JSON
    '''

    parent = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('name', 'parent', 'created_at', 'channel')


class ChannelSerializer(serializers.ModelSerializer):
    '''
        This serializer is used to represent a channel in JSON
    '''

    class Meta:
        model = Channel
        fields = ('name', 'created_at')
