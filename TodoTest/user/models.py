from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    age = models.CharField(max_length=50, default='', blank=True)
    description = models.CharField(max_length=100, default='', null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.username


