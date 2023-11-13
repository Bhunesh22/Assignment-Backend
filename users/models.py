import uuid
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db import IntegrityError, transaction
# from users.serializers import UserSerializer


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    USER_TYPE_CHOICE = (
        ('individual', 'individual'),
        ('team', 'team'),
    )

    BROKER_CHOICE = (
        ('Groww', 'Groww'),
        ('Zerodha', 'Zerodha'),
        ('Angel One', 'Angel One'),
        ('Upstox', 'Upstox'),
        ('ICICIdirect', 'ICICIdirect'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True,blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICE, blank=True)
    broker = models.CharField(max_length=100, choices=BROKER_CHOICE, blank=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.email)
