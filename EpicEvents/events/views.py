from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from clients.models import Client
from users.models import User
from contracts.models import Contract
from .serializers import (EventsListSerializer,
                           EventDetailSerializer,
                           ManagerEventCreationSerializer,
                           SaleEventCreationSerializer,
                           PartialUpdateEventCreationSerializer)
from .permission import SupportEventOrReadOnly
from .models import Event

class MultipleSerializerMixin:
    """ Return a specific serializer depending on the type of action """

    detail_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        elif self.action == 'update' and self.detail_serializer_class is not None:
            return self.update_serializer_class
        return super().get_serializer_class()


class EventsViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = EventsListSerializer
    detail_serializer_class = EventDetailSerializer
    update_serializer_class = PartialUpdateEventCreationSerializer
    queryset = Event.objects.all()

    permission_classes = [SupportEventOrReadOnly]

    """def get_queryset(self):
         Recover a specific queryset based on user status.

        if self.request.user.status == 'Management':
            queryset = Event.objects.all()
            return queryset

        elif self.request.user.status == 'Sale':
            queryset = Event.objects.filter(sale_user=self.request.user)
            return queryset

        elif self.request.user.status == 'Support':
            queryset = Event.objects.filter(support_user=self.request.user)
            return queryset"""


    def create(self, request, *args, **kwargs):
        """ Override create function and used a specific serializer based on
        user status. """

        if request.user.status == 'Management':
            serializer = ManagerEventCreationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

        elif request.user.status == 'Sale':
            serializer = SaleEventCreationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            contract = Contract.objects.filter(id=request.data['contract']).first()
            client = contract.client
            serializer.save(sale_user=request.user, client=client)


        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


