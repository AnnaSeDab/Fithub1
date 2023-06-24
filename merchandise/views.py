from django.shortcuts import render
from .models import Product


# Create your views here.


def merchandise(request):
    """A view to return the page with all the merchandise"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'merchandise/merchandise.html', context)
