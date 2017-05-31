from .views import PostViewSet, UserViewSet, AngerViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/post', PostViewSet)
router.register(r'api/user', UserViewSet)
router.register(r'api/anger', AngerViewSet)