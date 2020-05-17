from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import JSONField
from products.models import Product
from staff.models import StaffMember
# Create your models here.
class Sale(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)