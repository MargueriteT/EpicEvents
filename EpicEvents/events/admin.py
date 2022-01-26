from django.contrib import admin
from .models import Event
from .forms import EventSaleAdminForm, EventManagementAdminForm, \
    EventSupportAdminForm


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'id', 'contract', 'client', 'sale_user',
                    'support_user', 'event_date', 'status')

    search_fields = ('client__society_name', 'sale_user__username',
                     'support_user__username', 'event_title', 'status')

    def has_change_permission(self, request, obj=None):
        """ Set permission at object level """
        if obj is None:
            return True
        elif request.user.status == 'Management':
            return obj
        elif request.user.status == 'Support':
            return obj.support_user == request.user
        elif request.user.status == 'Sale':
            return obj.sale_user == request.user

    def get_form(self, request, obj=None, **kwargs):
        """ Display a form based on user status """

        if request.user.status == 'Management':
            kwargs['form'] = EventManagementAdminForm

        elif request.user.status == 'Sale':
            kwargs['form'] = EventSaleAdminForm

        elif request.user.status == 'Support':
            kwargs['form'] = EventSupportAdminForm

        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """ Save new event and updated event """

        if request.user.status == 'Management':
            super().save_model(request, obj, form, change)

        elif request.user.status == 'Sale':
            obj.status = 'New event'
            obj.client = obj.contract.client
            obj.sale_user = request.user
            super().save_model(request, obj, form, change)

        elif request.user.status == 'Support':
            super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if request.user.status == 'Sale':
            readonly_fields = ('client', 'sale_user', 'support_user', 'status')
            return readonly_fields

        elif request.user.status == 'Management':
            readonly_fields = ()
            return readonly_fields

        elif request.user.status == 'Support':
            readonly_fields = ('client', 'sale_user', 'support_user',
                               'contract')
            return readonly_fields

    def get_list_filter(self, request):
        """ Display filters based on user status """

        if request.user.status == 'Sale':
            list_filter = ('client__society_name', 'status')
            return list_filter

        elif request.user.status == 'Management':
            list_filter = ('client__society_name',
                           'support_user',
                           ('support_user', admin.EmptyFieldListFilter),
                           'sale_user__username',
                           'status')
            return list_filter

        elif request.user.status == 'Support':
            list_filter = ('client__society_name', 'status')
            return list_filter


admin.site.register(Event, EventAdmin)
