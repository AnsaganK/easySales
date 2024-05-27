from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from app.models import Product
from app.services.product import add_product


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        data = request.POST
        product = get_object_or_404(Product, id=data.get('product'))
        add_product(data, product, request.user.cart)
        messages.success(request, 'Товар добавлен в корзину')
        return redirect(product.subcategory.get_absolute_url())
