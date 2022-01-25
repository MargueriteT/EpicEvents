from django import forms
from .models import Event


class EventSaleAdminForm(forms.ModelForm):
    """ Form dysplay for sale user to create a new event. """

    class Meta:
        model = Event
        fields = ['event_title', 'contract', 'event_date']


class EventManagementAdminForm(forms.ModelForm):
    """ Form dysplay for manager to create a new event. """

    class Meta:
        model = Event
        fields = ['event_title', 'contract', 'sale_user', 'support_user',
                  'client', 'event_date', 'type', 'status']


class EventSupportAdminForm(forms.ModelForm):
    """ Form dysplay for support user to update an event. """

    class Meta:
        model = Event
        fields = ['event_title', 'event_date', 'type', 'status']
