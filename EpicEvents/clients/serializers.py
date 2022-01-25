from rest_framework import serializers
from .models import Client


class ClientsListSerializer(serializers.ModelSerializer):
    """ Serialize datas to display clients as a list.  """

    class Meta:
        model = Client
        fields = ['id', 'society_name', 'is_a_client']


class ClientDetailSerializer(serializers.ModelSerializer):
    """ Serialize details about a specific client.  """

    class Meta:
        model = Client
        fields = ['id', 'society_name', 'is_a_client', 'number', 'street',
                  'zip_code', 'city_name', 'phonenumber', 'email']






