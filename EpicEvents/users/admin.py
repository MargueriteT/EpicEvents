from django.contrib import admin
from .models import User
from .forms import UserAdminForm


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "first_name", "last_name", "status",
                    "is_staff")
    list_filter = ("status",)

    def get_form(self, request, obj=None, **kwargs):
        """ Display the form to create or update an user. """

        return UserAdminForm

    def save_model(self, request, obj, form, change):
        """ Save new or updated user. """

        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)

