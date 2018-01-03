from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include('channels.urls', namespace='channels')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
