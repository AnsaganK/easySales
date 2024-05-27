from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse


@login_required
def cart_detail(request):
    user = request.user
    cart = user.cart

    return render(request, 'app/cart/detail.html', {
        'cart': cart,
        'cart_items': cart.items.all(),
    })


@login_required
def delete_cart_item(request, product_id: int):
    cart = request.user.cart
    item = cart.items.filter(product_id=product_id)
    item.delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect(reverse('app:cart_detail'))
