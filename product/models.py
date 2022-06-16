from django.db import models
from users.models import Seller


class Product(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField(primary_key=True)
    pic = models.URLField()
    price = models.IntegerField()
    rating = models.PositiveIntegerField(default=0)
    product_type = models.CharField(max_length=15)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)

    def create(self, name, pic, number, price, pr_type, seller):
        self.name = name
        self.number = number
        self.pic = pic
        self.price = price
        self.product_type = pr_type
        self.seller = seller
