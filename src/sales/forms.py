from django import forms
from .models import Sale
from products.models import Product
from orders.models import Order
from django.contrib.postgres.fields import JSONField
class StaffForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'staff_member',
        ]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'item'
        ]
