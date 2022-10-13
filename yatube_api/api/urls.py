from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path(r'v1/', include(router.urls)),
]
