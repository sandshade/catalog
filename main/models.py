from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=255)

class Color(models.Model):
    title = models.CharField(max_length=255)
    rbg = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    links = models.ManyToManyField(Link, blank=True, related_name="pictures")
    quantity = models.IntegerField()
    colors = models.ManyToManyField(Color, blank=True, related_name="colors")
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    date = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    orderedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ordered_by")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ordered_products")
    quantity = models.IntegerField()
