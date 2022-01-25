from django import forms
from .models import User


class UserAdminForm(forms.ModelForm):
    """ Form display to create or update an user. """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'status',
                  'password']

    def clean(self):
        """ Cleaned data """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        return cleaned_data

    def save(self, commit=True):
        """ Save the provided password in hashed format """

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user