from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_detail_view(request, *argsm, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    else:
        for field in form.errors:
            form[field].field.widget.attrs['class'] = 'error'

    context = {
        'products': Product.objects.order_by('id'),
        'form': form
    }
    return render(request, 'products/products.html', context)