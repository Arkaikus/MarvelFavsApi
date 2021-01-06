from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from api.models import Favorites


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('comicId', 'title', 'thumbnail')




