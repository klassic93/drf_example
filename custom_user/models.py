from django.db import models


class CustomUser(models.Model):
    username = models.CharField(verbose_name='name', unique=True, max_length=100)
