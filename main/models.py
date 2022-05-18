from tabnanny import verbose
from unicodedata import category
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Doctor(models.Model):
    category = models.ForeignKey(Category, related_name='doctors', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'