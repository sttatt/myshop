from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image_source = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

