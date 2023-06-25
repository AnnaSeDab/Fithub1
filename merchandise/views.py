from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def merchandise(request):
    """A view to return the page with all the merchandise"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'merchandise/merchandise.html', context)


def product_detail(request, product_id):
    """A view to return the page with chosen product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'merchandise/product_detail.html', context)
