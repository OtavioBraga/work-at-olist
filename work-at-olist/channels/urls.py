from django.contrib.auth import views as auth_views
from channels.views import CategoriesList, ChannelsList
from django.conf.urls import url

urlpatterns = [

    url(r'^category/',
        CategoriesList.as_view(),
        name='categories-list'),

    url(r'^channel/',
        ChannelsList.as_view(),
        name='channels-list')

]
