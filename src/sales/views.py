from django.shortcuts import render
from .models import Sale
from .forms import StaffForm, ItemForm, DateForm #,SaleForm
from products.models import Product
from staff.models import StaffMember
from orders.models import Order
from classes.report import ReportItem
# Create your views here.
items = []
reports = []

def getProducts():
    return map(
        (lambda model: (model.id, model.name)), 
        Product.objects.all()
    )

def getStaff():
    return map(
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
        'products': getProducts(),
        'staff': getStaff(),
        'items': items,
        'item_form': item_form,
        'staff_form': staff_form
    }


    return render(request, 'sales/sale_form.html', context)

def report_form_view(request):

    staff_form = StaffForm(request.POST or None)
    date_form = DateForm(request.POST or None)
    total = 0
    total_commission = 0

    if staff_form.is_valid() and date_form.is_valid():# and request.POST.get('end_date') >= request.POST.get('start_date'):
        staff_member = StaffMember.objects.get(id=int(request.POST.get('staff_member')))
        reports.clear()
        total = 0
        total_commission = 0

        sales = Sale.objects.filter(
            date__date__range=[
                date_form.cleaned_data['start_time'],
                date_form.cleaned_data['end_time']
            ], 
            staff_member_id=staff_member
        )

        for sale in sales:
            orders = Order.objects.filter(sale_id=sale.id)
            report_item = ReportItem(staff_member, sale.date, orders)
            reports.append(report_item)

        for report in reports:
            total += report.total_price
            total_commission += report.commission

        staff_form = StaffForm()
        date_form = DateForm()

    else:
        reports.clear()
        for field in staff_form.errors:
            staff_form[field].field.widget.attrs['class'] = 'error'

        for field in date_form.errors:
            date_form[field].field.widgets.attrs['class'] = 'error'

    context = {
        'staff_form': staff_form,
        'date_form': date_form,
        'staff': getStaff(),
        'reports': reports,
        'total_price': total,
        'total_commission': total_commission
    }
    return render(request, 'sales/report_form.html', context)