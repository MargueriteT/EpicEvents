from django.contrib import admin
from .models import Client
from .forms import ClientSaleAdminForm, ClientManagementAdminForm
from events.models import Event

class ClientAdmin(admin.ModelAdmin):

    list_display = ('society_name', 'id', 'city_name', 'email', 'phonenumber',
                    'is_a_client', 'sale_user')

    search_fields = ('society_name', 'city_name', 'is_a_client')

    def get_queryset(self, request):
        """ Recover a specific queryset based on user status. """
        queryset = super(ClientAdmin, self).get_queryset(request)
        if request.user.status == 'Support':
            events = Event.objects.filter(support_user=request.user)
            clients_id = []
            for event in events:
                clients_id.append(event.client.id)
            return queryset.filter(id__in=clients_id)
        return queryset

    def get_form(self, request, obj=None, **kwargs):
        """
        Display a form to create or update a client based on user status.
        """

        if request.user.status == 'Management':
            kwargs['form'] = ClientManagementAdminForm

        elif request.user.status == 'Sale':
            kwargs['form'] = ClientSaleAdminForm

        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """ Save new event and updated client """

        if request.user.status == 'Management':
            super().save_model(request, obj, form, change)

        elif request.user.status == 'Sale' and obj.is_a_client is True:
            obj.sale_user = request.user
            super().save_model(request, obj, form, change)

    def get_list_filter(self, request):
        """ Display filters based on user status """

        if request.user.status == 'Sale':
            list_filter = ('is_a_client', 'city_name',
                           ('sale_user', admin.EmptyFieldListFilter),)
            return list_filter

        elif request.user.status == 'Management':
            list_filter = ('is_a_client',
                           'city_name',
                           ('sale_user', admin.EmptyFieldListFilter),)
            return list_filter

        elif request.user.status == 'Support':
            list_filter = ('is_a_client', 'city_name',)
            return list_filter


admin.site.register(Client, ClientAdmin)

