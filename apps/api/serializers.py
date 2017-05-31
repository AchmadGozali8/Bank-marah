from apps.models import Post, Anger
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, ValidationError

class PostSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('url', 'user', 'anger', 'description', 'created_at', 'updated_at')


class UserSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')


class AngerSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Anger
		fields = ('url', 'description')
