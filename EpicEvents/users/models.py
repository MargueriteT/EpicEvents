from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager, Group


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """ Create and save a user with the given username, email, and
        password. """

        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """Create a superuser with staff and superuser status set to False"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None,
                         **extra_fields):
        """Create a superuser with staff and superuser status set to True"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Define all attributs for an instance of an user. """

    MANAGEMENT = 'Management'
    SALE = 'Sale'
    SUPPORT = 'Support'

    STATUS_CHOICES = (
        (MANAGEMENT, 'MANAGEMENT'),
        (SALE, 'SALE'),
        (SUPPORT, 'SUPPORT'),
    )
    username = models.CharField(verbose_name='username',
                                max_length=150,
                                unique=True)

    first_name = models.CharField(verbose_name='first name',
                                  max_length=150,
                                  blank=False)

    last_name = models.CharField(verbose_name='last name',
                                 max_length=150,
                                 blank=False)

    email = models.EmailField(verbose_name='email address',
                              blank=False)

    status = models.CharField(max_length=30,
                              choices=STATUS_CHOICES,
                              verbose_name='status',
                              default=MANAGEMENT)

    is_staff = models.BooleanField(verbose_name='is_staff',
                                   default=True)

    is_active = models.BooleanField(verbose_name='is_active',
                                    default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'last_name', 'first_name']

    def save(self, *args, **kwargs):
        """ Save the user instance and assign the user to the group
        corresponding to his status. """

        super().save(*args, **kwargs)

        if self.status == self.MANAGEMENT:
            group = Group.objects.get(name='management')
            group.user_set.add(self)

        elif self.status == self.SALE:
            group = Group.objects.get(name='sale')
            group.user_set.add(self)

        elif self.status == self.SUPPORT:
            group = Group.objects.get(name='support')
            group.user_set.add(self)

