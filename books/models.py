from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from custom_user.models import CustomUser


class Book(models.Model):
    name = models.CharField(verbose_name='book_name', unique=True, max_length=100)
    popularity = models.BigIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    user = models.ForeignKey(CustomUser, related_name='books', null=True, on_delete=models.SET_NULL)
