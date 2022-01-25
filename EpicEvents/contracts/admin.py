from django.contrib import admin
from .models import Contract
from .forms import ContractManagementAdminForm, ContractSaleAdminForm


class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'client', 'created', 'sale_user', 'signed')
    search_fields = ('client__society_name', 'sale_user__username')

    def get_queryset(self, request):
        """ Recover the queryset to display based on user status. A sale
        user can access only his own contracts however a manager can access
        all contracts. """

        queryset = super(ContractAdmin, self).get_queryset(request)
        if request.user.status == 'Sale':
            return queryset.filter(sale_user=request.user)

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        """ Display a form to create a new contract or update it based on
        user status """

        if request.user.status == 'Management':
            kwargs['form'] = ContractManagementAdminForm

        elif request.user.status == 'Sale':
            kwargs['form'] = ContractSaleAdminForm

        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """ Save new or updated instance based on user status. For a seller,
        the creation of contract will set him as sale_user """

        if request.user.status == 'Management':
            super().save_model(request, obj, form, change)

        elif request.user.status == 'Sale':
            obj.sale_user = request.user
            super().save_model(request, obj, form, change)

    def get_list_filter(self, request):
        """ Display filters based on user status """

        if request.user.status == 'Sale':
            list_filter = ('client', 'signed')
            return list_filter

        elif request.user.status == 'Management':
            list_filter = ('client',
                           'sale_user',
                           'signed')
            return list_filter


admin.site.register(Contract, ContractAdmin)
