from django.contrib.auth import views as auth_views
from channels.views import (
    CategoriesListView, ChannelsListView, ChannelDetailView, CategoryDetailView
)
from django.urls import path


app_name = "channels"

urlpatterns = [

    path('category/', CategoriesListView.as_view(), name='categories-list'),

    path('channel/', ChannelsListView.as_view(), name='channels-list'),

    path('channel/<uuid:uuid>/',
         ChannelDetailView.as_view(),
         name='channel-detail'),

    path('category/<uuid:uuid>/',
         CategoryDetailView.as_view(),
         name='category-detail')

]
