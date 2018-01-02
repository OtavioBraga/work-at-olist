from channels.serializers import CategorySerializer, ChannelSerializer
from channels.models import Category, Channel
from rest_framework import generics


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChannelsList(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
