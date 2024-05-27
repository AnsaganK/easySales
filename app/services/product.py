from django.shortcuts import get_object_or_404

from app.models import Product, CartItem


def add_product(data: dict, product, cart, via: CartItem.ViaChoices = CartItem.ViaChoices.SITE.value):
    cart_item = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )
    if cart_item[1]:
        cart_item[0].save()
    cart_item = cart_item[0]
    cart_item.quantity = data.get('quantity')
    cart_item.via = via
    cart_item.save()
