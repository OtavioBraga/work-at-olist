from channels.serializers import CategorySerializer, ChannelSerializer
from channels.models import Category, Channel
from rest_framework import generics


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all().select_related('parent', 'channel')
    serializer_class = CategorySerializer


class ChannelsListView(generics.ListAPIView):
    queryset = Channel.objects.all().prefetch_related('category_set')
    serializer_class = ChannelSerializer


class ChannelDetailView(generics.RetrieveAPIView):
    queryset = Channel.objects.all().prefetch_related('category_set')
    serializer_class = ChannelSerializer
    lookup_field = 'uuid'


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all().select_related('parent', 'channel')
    serializer_class = CategorySerializer
    lookup_field = 'uuid'
