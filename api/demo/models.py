from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    categories = models.ManyToManyField(Category, db_table="product_category")
    class Meta:
        db_table = 'product'

class Order(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, db_table="order_product")
    class Meta:
        db_table = 'order'