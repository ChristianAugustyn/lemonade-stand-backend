from django.db import models

from products.models import Product
from staff.models import StaffMember
# Create your models here.
class Sale(models.Model):
    PRODUCTS = map( #not needed
        (lambda model: (model.id, model.name)), 
        Product.objects.all()
    )

    STAFF = map( #not needed
        (lambda model: (model.id, ' '.join([model.first_name, model.last_name]))),
        StaffMember.objects.all()
    )

    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)