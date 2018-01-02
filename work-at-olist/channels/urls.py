from django.contrib.auth import views as auth_views
from channels.views import CategoriesList, ChannelsList, ChannelDetail
from django.urls import path


app_name = "channels"

urlpatterns = [

    path('category/', CategoriesList.as_view(), name='categories-list'),

    path('channel/', ChannelsList.as_view(), name='channels-list'),

    path('channel/<uuid:uuid>/', ChannelDetail.as_view(), name='channel-detail')

]
