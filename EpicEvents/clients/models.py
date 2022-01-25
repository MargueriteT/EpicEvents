from django.db import models
from users.models import User


class Client(models.Model):
    """ Define all attributs for an instance of client. """

    society_name = models.CharField(verbose_name='society_name',
                                    unique=True,
                                    max_length=150, blank=False)

    number = models.IntegerField(verbose_name='Number',
                                 null=False,
                                 default=1)

    street = models.CharField(verbose_name='street',
                              max_length=150,
                              blank=False,
                              default='fake street')

    zip_code = models.IntegerField(verbose_name='zip code',
                                   null=False,
                                   default=75000)

    city_name = models.CharField(verbose_name='city',
                                 max_length=100,
                                 blank=False,
                                 default='Paris')

    email = models.EmailField(verbose_name='email',
                              max_length=150,
                              blank=False,
                              default='fake@mail.com')

    phonenumber = models.CharField(verbose_name='phone number',
                                   max_length=10,
                                   blank=False,
                                   default='xxxxxxxxxx')

    is_a_client = models.BooleanField(verbose_name='is a client',
                                      default=False)
    if is_a_client:
        sale_user = models.ForeignKey(User,
                                      limit_choices_to={
                                          'groups__name': 'sale'},
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True)

    def __str__(self):
        """ Return the society's name to facilitate instance description. """

        return self.society_name
