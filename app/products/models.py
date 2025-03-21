from django.db import models

from authentication.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Товары'
        verbose_name = ' Товар'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()
    name = models.CharField(max_length=100)


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
