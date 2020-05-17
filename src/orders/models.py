from django.db import models
from sales.models import Sale
from products.models import Product
# Create your models here.
class Order(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)