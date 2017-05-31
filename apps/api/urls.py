from django.conf.urls import url, include
from .router import router

urlpatterns = [
    url(r'^', include(router.urls)),
]