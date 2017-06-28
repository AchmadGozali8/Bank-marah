from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, UserSerializer, AngerSerializer
from apps.models import Post, Anger
from django.contrib.auth.models import User

class PostPagination(PageNumberPagination):
        page_size = 100
        page_size_query_param = 'page'


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all().order_by('-id')
	serializer_class = PostSerializer
        pagination_class = PostPagination


class UserViewSet(ModelViewSet):
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserSerializer


class AngerViewSet(ModelViewSet):
	queryset = Anger.objects.all().order_by('-id')
	serializer_class = AngerSerializer
