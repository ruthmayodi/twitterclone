from django.db import models
from django.contrib.auth.models import (AbstractUser)


class TwitterUser(AbstractUser):
    followed = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

