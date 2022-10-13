from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls import path
'''from rest_framework.routers import SimpleRouter
from yatube_api.api.views import PostViewSet, GroupViewSet'''

'''router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
