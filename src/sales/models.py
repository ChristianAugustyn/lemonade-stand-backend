from datetime import datetime
from django.db import models
from products.models import Product
from staff.models import StaffMember
# Create your models here.
class Sale(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)