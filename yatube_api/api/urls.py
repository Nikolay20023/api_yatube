from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views


router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/api-token-auth/', views.obtain_auth_token)
]
