from rest_framework import serializers
from .models import User


class UsersListSerializer(serializers.ModelSerializer):
    """ Serialize datas of users to dispay them as a list. """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'status']


class UserDetailSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific user. """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'status', 'is_active', 'is_staff']


class UserCreationSerializer(serializers.ModelSerializer):
    """ Serializer used for the creation of a new instance of user by a
    manager. """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'status', 'password']


class UserPartialUpdateSerializer(serializers.ModelSerializer):
    """ Serializer used to update an instance of user by a manager. """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'status']