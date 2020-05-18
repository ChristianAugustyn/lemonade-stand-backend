from django import forms
from .models import Sale
from products.models import Product
from orders.models import Order
from datetime import date

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

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_time = forms.DateField(
        widget=DateInput(attrs={'class': ''}), 
        required=True,
    )
    end_time = forms.DateField(
        widget=DateInput(attrs={'class': ''}), 
        required=True
    )

