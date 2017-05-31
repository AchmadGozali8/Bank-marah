from django.contrib.auth.models import User
from .models import Anger, Post
from rest_framework import serializer


class UserSerializer(serializer.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')

class AngerSerializer(serializer.HyperlinkedModelSerializer):
	class Meta:
		model = Anger
		fields = ('level')

class PostSerializer(serializer.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('user', 'anger', 'description', 'created_at', )