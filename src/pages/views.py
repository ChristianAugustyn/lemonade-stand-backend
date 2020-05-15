from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from staff.models import StaffMember
from products.models import Product
# Create your views here.
def form_view(request, *args, **kwargs):
    context = { #contexts are used for passing info to the template, python dicts
        'staff': StaffMember.objects.order_by('commission')
    }
    return render(request, 'form.html', context)