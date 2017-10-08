from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
