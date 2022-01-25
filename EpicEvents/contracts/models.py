from django.db import models
from users.models import User
from clients.models import Client


class Contract(models.Model):
    """ Define all attributs for an instance of contract. """

    title = models.CharField(verbose_name='Contract title',
                             max_length=250,
                             default='default title')

    sale_user = models.ForeignKey(User,
                                  limit_choices_to={'groups__name': 'sale'},
                                  on_delete=models.CASCADE)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    created = models.DateField(verbose_name='Date of creation',
                               auto_now_add=True)

    content = models.TextField(verbose_name='content of the contract')

    signed = models.BooleanField(verbose_name='Contract is signed?',
                                 default=False)

    def __str__(self):
        """ Return the title of the contract to facilitate instance
        description. """

        return self.title
