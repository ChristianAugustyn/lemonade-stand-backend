from django.shortcuts import render
from .models import Sale
from .forms import StaffForm, ItemForm #,SaleForm
from products.models import Product
from staff.models import StaffMember
from orders.models import Order
# Create your views here.
items = []

PRODUCTS = map( #not needed
    (lambda model: (model.id, model.name)), 
    Product.objects.all()
)

STAFF = map( #not needed
    (lambda model: (model.id, ' '.join([model.first_name, model.last_name]))),
    StaffMember.objects.all()
)

def sale_form_view(request, *args, **kwargs):

    item_form = ItemForm(request.POST or None)
    staff_form = StaffForm(request.POST or None)

    if item_form.is_valid():
        items.append(request.POST.get('item'))
        item_form = ItemForm()

    if staff_form.is_valid() and len(items) > 0:

        sale = Sale.objects.create(
            staff_member=StaffMember.objects.get(id=int(request.POST.get('staff_member'))),
            # item=Product.objects.get(id=int(i))
        )
        sale.save()
        for i in items:
            order = Order.objects.create(
                sale=sale,
                item=Product.objects.get(id=int(i))
            )
            order.save()
        items.clear()
        item_form = ItemForm()
        staff_form = StaffForm()
    
    context = {
        'products': PRODUCTS,
        'staff': STAFF,
        'items': items,
        'item_form': item_form,
        'staff_form': staff_form
    }

    return render(request, 'sales/sale_form.html', context)

def report_form_view(request):

    staff_form = StaffForm(request.POST or None)

    print(request.POST)

    context = {
        'staff_form': staff_form,
        'staff': STAFF,
    }
    return render(request, 'sales/report_form.html', context)