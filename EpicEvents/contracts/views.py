from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from clients.models import Client
from users.models import User
from .serializers import (ContractsListSerializer,
                          ContractDetailSerializer,
                          SaleUserContractCreationSerializer,
                          ManagerUserContractCreationSerializer)
from .permission import (SaleContractOrReadOnly,
                         ManagementContractOrReadOnly,
                         SupportContractOrReadOnly)
from .models import Contract


class MultipleSerializerMixin:
    """ Return the detail serializer when action is retrieve """

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AllContractsViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractsListSerializer
    detail_serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()
    permission_classes = (SaleContractOrReadOnly | ManagementContractOrReadOnly |SupportContractOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """ Override create function and used a specific serializer based on
        user status. """

        if request.user.status == 'Management':
            serializer = ManagerUserContractCreationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

        elif request.user.status == 'Sale':
            serializer = SaleUserContractCreationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(sale_user=request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



