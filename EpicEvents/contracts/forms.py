from django import forms
from .models import Contract


class ContractSaleAdminForm(forms.ModelForm):
    """ Form dysplay for sale user to create or update a contract. """

    class Meta:
        model = Contract
        fields = ['title', 'client', 'content', 'signed']


class ContractManagementAdminForm(forms.ModelForm):
    """ Form dysplay for manager to create or update a contract. """

    class Meta:
        model = Contract
        fields = ['title', 'client', 'sale_user', 'content', 'signed']

