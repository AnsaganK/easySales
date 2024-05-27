from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def cart_detail(request):
    user = request.user
    cart = user.cart

    return render(request, 'app/cart/detail.html', {
        'cart': cart
    })
