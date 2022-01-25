from rest_framework import serializers
from .models import Event
from clients.models import Client
from users.models import User
from contracts.models import Contract


class ClientSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific client - used in the other
    serializer to display the client linked to the event. """

    class Meta:
        model = Client
        fields = ['id', 'society_name']


class SaleSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific seller - used in the other
    serializer to display the client linked to the event. """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'status']


class SupportSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific support user - used in the other
    serializer to display the client linked to the event. """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'status']


class EventsListSerializer(serializers.ModelSerializer):
    """ Serialize datas of events to dispay them as a list. """

    client = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'contract', 'client', 'event_date', 'type', 'status']

    def get_client(self, instance):
        contract = instance.contract
        contract = Contract.objects.filter(id=contract.id).first()
        serializer = ClientSerializer(contract.client, many=False)
        return serializer.data


class EventDetailSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific event. """

    client = serializers.SerializerMethodField()
    sale = serializers.SerializerMethodField()
    support = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'contract', 'sale', 'support', 'client', 'event_date',
                  'type', 'status']

    def get_client(self, instance):
        contract = instance.contract
        contract = Contract.objects.filter(id=contract.id).first()
        serializer = ClientSerializer(contract.client, many=False)
        return serializer.data

    def get_sale(self, instance):
        user = User.objects.filter(id=instance.sale_user.id).first()
        serializer = SaleSerializer(user, many=False)
        return serializer.data

    def get_support(self, instance):
        try:
            user = User.objects.filter(id=instance.support_user.id).first()
            serializer = SupportSerializer(user, many=False)
            return serializer.data
        except AttributeError:
            return 'Event to be assigned '


class SaleEventCreationSerializer(serializers.ModelSerializer):
    """ Serializer used for the creation of a new instance of event by a
    seller. """

    class Meta:
        model = Event
        fields = ['event_title', 'contract', 'event_date', 'type']


class ManagerEventCreationSerializer(serializers.ModelSerializer):
    """ Serializer used for the creation of a new instance of event by a
    manager. """

    class Meta:
        model = Event
        fields = ['sale_user', 'support_user', 'event_title', 'contract',
                  'event_date', 'type']


class PartialUpdateEventCreationSerializer(serializers.ModelSerializer):
    """ Serializer used to update an instance of event by a support
    user. """

    class Meta:
        model = Event
        fields = ['event_title', 'event_date', 'type', 'status']