from rest_framework import serializers
from .models import Contract
from clients.models import Client
from users.models import User


class ClientSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific client - used in the other
    serializer to display the client linked to the contract. """

    class Meta:
        model = Client
        fields = ['id', 'society_name', 'is_a_client']


class UserSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific user - used in the other
    serializer to display the user linked to the contract. """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'status']


class ContractsListSerializer(serializers.ModelSerializer):
    """ Serialize datas of contracts to dispay them as a list. """

    sale_user = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'title', 'sale_user', 'client', 'created', 'signed']

    def get_sale_user(self, instance):
        user = instance.sale_user
        serializer = UserSerializer(user, many=False)
        return serializer.data

    def get_client(self, instance):
        client = instance.client
        serializer = ClientSerializer(client, many=False)
        return serializer.data


class ContractDetailSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific contract """

    sale_user = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'title', 'sale_user', 'client', 'created', 'content',
                  'signed']

    def get_sale_user(self, instance):
        user = instance.sale_user
        serializer = UserSerializer(user, many=False)
        return serializer.data

    def get_client(self, instance):
        client = instance.client
        serializer = ClientSerializer(client, many=False)
        return serializer.data


class SaleUserContractCreationSerializer(serializers.ModelSerializer):
    """ Serializer used for the creation of a new instance of contract by a
    sale user. """

    class Meta:
        model = Contract
        fields = ['client', 'title', 'content', 'signed']


class ManagerUserContractCreationSerializer(serializers.ModelSerializer):
    """ Serializer used for the creation of a new instance of contract by a
    manager. """

    class Meta:
        model = Contract
        fields = ['id', 'title', 'sale_user', 'client', 'created', 'content',
                  'signed']


