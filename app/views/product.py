from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse, get_object_or_404

from app.forms.cart import CartItemForm


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart = request.user.cart
            cart_item.cart = cart
            cart_item.save()
            messages.success(request, 'Товар добавлен в корзину')
        else:
            print(form.errors)
            messages.error(request, 'Неправильно заполненная форма')
        return redirect(reverse('app:home'))
