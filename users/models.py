from django.db import models
from django.contrib.auth.models import User


class Client(User):
    pass


class Seller(User):
    country = models.CharField(max_length=10)
    rating = models.PositiveIntegerField(default=0)

    def add_product(self, product):
        self.products_set.add(product)
