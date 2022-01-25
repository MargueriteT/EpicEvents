from django import forms
from .models import Client


class ClientSaleAdminForm(forms.ModelForm):
    """ Form dysplay for sale user to create or update a client. """

    class Meta:
        model = Client
        fields = ['society_name', 'number', 'street', 'zip_code', 'city_name',
                  'email', 'phonenumber', 'is_a_client']


class ClientManagementAdminForm(forms.ModelForm):
    """ Form dysplay for a manager to create or update a client. """

    class Meta:
        model = Client
        fields = ['society_name', 'number', 'street', 'zip_code', 'city_name',
                  'email', 'phonenumber', 'is_a_client', 'sale_user']

