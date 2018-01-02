from rest_framework import serializers
from channels.models import Category, Channel


class CategorySerializer(serializers.ModelSerializer):
    '''
        This serializer is used to represent a category in JSON
    '''

    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'parent', 'uuid')

    def get_parent(self, category):
        if category.parent is not None:
            return CategorySerializer(category.parent).data
        else:
            return None


class ChannelSerializer(serializers.ModelSerializer):
    '''
        This serializer is used to represent a channel in JSON.
    '''

    link = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='channels:channel-detail',
        source='uuid',
        lookup_field='uuid'
    )

    category_set = CategorySerializer(many=True)

    class Meta:
        model = Channel
        fields = ('name', 'uuid', 'category_set', 'link')
