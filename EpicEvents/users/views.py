from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import ( UsersListSerializer,
                           UserDetailSerializer,
                           UserCreationSerializer )
from .models import User
from .permission import UserPermission


class MultipleSerializerMixin:
    """ Return a specific serializer depending on the type of action """

    detail_serializer_class = None
    create_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create' and self.create_serializer_class is not None:
            return self.create_serializer_class

        elif self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AllUsersViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = UsersListSerializer
    detail_serializer_class = UserDetailSerializer
    create_serializer_class = UserCreationSerializer


    permission_classes = [UserPermission]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        """ Override create function. """

        serializer = UserCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=request.data['username'],
                                        first_name=request.data['first_name'],
                                        last_name=request.data['last_name'],
                                        email= request.data['email'],
                                        status=request.data['status'],
                                        password=request.data['password'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)




