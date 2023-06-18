from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True, null=False)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Categories', to_field='category_name', on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey('Company', to_field='company_name', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.item_name


class Cheque(models.Model):
    item_id = models.IntegerField(null=True)
    item_name = models.ForeignKey(Item, to_field='item_name', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.item_name


class Purchases(models.Model):
    customer_id = models.ForeignKey(User, to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    cheque_id = models.ForeignKey(Cheque, to_field='id', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.pk


class Deliveries(models.Model):
    item_name = models.ForeignKey(Item, to_field='item_name', on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.item_name


class Categories(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.company_name
