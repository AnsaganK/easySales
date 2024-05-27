from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializers.product import ProductSerializer
from app.models import SubCategory, Product


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
