from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from events.models import Event
from .serializers import ClientsListSerializer,ClientDetailSerializer
from .permission import ClientPermission
from .models import Client

class MultipleSerializerMixin:
    """ Return a specific serializer depending on the type of action """

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        elif self.action == 'update' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        elif self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class ClientsViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ClientsListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [ClientPermission]

    def get_queryset(self):
        """ Recover a specific queryset based on user status. """

        if self.request.user.status == 'Management' or \
            self.request.user.status == 'Sale':
            queryset = Client.objects.all()
            return queryset

        elif self.request.user.status == 'Support':
            events = Event.objects.filter(support_user=self.request.user)
            clients_id = []
            for event in events:
                clients_id.append(event.client.id)
            queryset = Client.objects.filter(id__in=clients_id)
            return queryset






