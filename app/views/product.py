from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse, get_object_or_404

from app.forms.cart import CartItemForm
from app.models import Product, CartItem


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=request.POST.get('product'))
        cart_item = CartItem.objects.get_or_create(
            cart=request.user.cart,
            product=product
        )
        if cart_item[1]:
            cart_item[0].save()
        cart_item = cart_item[0]
        cart_item.quantity = request.POST.get('quantity')
        cart_item.save()
        messages.success(request, 'Товар добавлен в корзину')
        return redirect(product.subcategory.get_absolute_url())
