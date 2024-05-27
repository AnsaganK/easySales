from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializers.product import ProductSerializer
from app.models import SubCategory, Product, CartItem, Cart
from app.services.product import add_product


@api_view(["GET"])
def product_list(request, slug):
    subcategory = get_object_or_404(SubCategory, slug=slug)
    products = subcategory.products.all()
    paginator = PageNumberPagination()
    paginator.page_size = 9
    products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(products, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_to_cart(request):
    data = request.data
    product_id = int(data.get('product'))
    telegram_id = data.get('telegram_id')
    cart = Cart.objects.filter(user__profile__telegram_id=telegram_id).first()
    product = get_object_or_404(Product, id=product_id)
    if cart:
        add_product(data, product, cart, CartItem.ViaChoices.TELEGRAM.value)
        return Response({
            'message': f'Товар <b>"{product.name.upper()}"</b> добавлен в корзину'
        }, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Товар не добавлен в корзину'}, status=status.HTTP_404_NOT_FOUND)
