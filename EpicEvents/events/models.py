from django.db import models
from contracts.models import Contract
from users.models import User
from clients.models import Client


class Event(models.Model):
    """ Define all attributs for an instance of event. """

    NEW = 'New event'
    IN_PROGRESS = 'In progress'
    FINISHED = 'Finished'

    STATUS_CHOICES = (
        (NEW, 'NEW'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (FINISHED, 'FINISHED'),
    )

    event_title = models.CharField(verbose_name='Event Title',
                                   max_length=250,
                                   default='default title')

    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)

    sale_user = models.ForeignKey(User,
                                  limit_choices_to={'groups__name': "sale"},
                                  on_delete=models.CASCADE,
                                  related_name='sale')

    support_user = models.ForeignKey(User,
                                     limit_choices_to={
                                         'groups__name': "support"},
                                     on_delete=models.CASCADE,
                                     related_name='support',
                                     null=True,
                                     blank=True)

    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    event_date = models.DateTimeField(verbose_name='date of the event')

    type = models.TextField(verbose_name='event organisation')

    status = models.CharField(max_length=30,
                              choices=STATUS_CHOICES,
                              verbose_name='status',
                              default=NEW)

    def __str__(self):
        """ Return the event's title to facilitate instance description. """
        return self.event_title