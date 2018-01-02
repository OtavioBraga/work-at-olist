from rest_framework import serializers
from channels.models import Category, Channel


class ResumedChannelSerializer(serializers.HyperlinkedModelSerializer):
    '''
        This serializer is a resumed version of ChannelSerializer,
        only to display the channel on a category.
    '''

    link = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='channels:channel-detail',
        source='uuid',
        lookup_field='uuid'
    )

    class Meta:
        model = Channel
        fields = ('name', 'link')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''
        This serializer is used to represent a category in JSON
    '''

    parent = serializers.SerializerMethodField()

    link = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='channels:category-detail',
        source='uuid',
        lookup_field='uuid'
    )

    channel = ResumedChannelSerializer()

    class Meta:
        model = Category
        fields = ('name', 'parent', 'link', 'channel')

    def get_parent(self, category):
        if category.parent is not None:
            return CategorySerializer(
                category.parent,
                context={'request': self.context['request']}
            ).data
        return None


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
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
