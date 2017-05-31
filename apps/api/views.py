from rest_framework.view import ModelViewSet
from .serializers import PostSerializer, UserSerializer, AngerSerializer
from apps.models import Post, Anger
from django.contrib.auth.models import User

class PostViewSet(ModelViewSet):
	queryset = Post.objects.all().order_by('-id')
	serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserSerializer


class AngerViewSet(ModelViewSet):
	queryset = Anger.objects.all().order_by('-id')
	serializer_class = AngerSerializer
