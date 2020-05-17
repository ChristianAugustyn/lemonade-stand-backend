from django.shortcuts import render
from .models import Sale
from .forms import StaffForm, ItemForm #,SaleForm
from products.models import Product
from staff.models import StaffMember
from orders.models import Order
from classes.report import ReportItem
# Create your views here.
items = []
reports = []

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

    if staff_form.is_valid() and request.POST.get('end-date') >= request.POST.get('start-date'):
        print(request.POST)
        staff_form = StaffForm()
        reports.clear()
        staff_member = StaffMember.objects.get(id=int(request.POST.get('staff_member')))

        sales = Sale.objects.filter(
            date__date__range=[
                request.POST.get('start-date'),
                request.POST.get('end-date')
            ], 
            staff_member_id=staff_member
        )

        for sale in sales:
            orders = Order.objects.filter(sale_id=sale.id)
            report_item = ReportItem(staff_member, sale.date, orders)
            reports.append(report_item)

    context = {
        'staff_form': staff_form,
        'staff': STAFF,
        'reports': reports
    }
    return render(request, 'sales/report_form.html', context)