from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class TestUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True, db_index=True)

    USERNAME_FIELD = 'identifier'

    def get_full_name(self):
        return self.identifier

    def get_short_name(self):
        return self.identifier


class TestProfile(models.Model):
    """
    A user profile model for use by unit tests. This has nothing to do with the
    authentication backend itself.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    populated = models.BooleanField(default=False)
