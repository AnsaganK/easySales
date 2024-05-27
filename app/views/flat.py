from django.contrib import messages
from django.shortcuts import render

from app.models import Product


def home(request):
    return render(request, 'app/flat/home.html', {
        'popular_products': Product.objects.order_by('?')[:8],
    })
