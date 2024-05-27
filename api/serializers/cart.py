from decimal import Decimal

from django.db import models
from django.db.models import Sum, F
from rest_framework import serializers

from app.models import Cart, CartItem, Product


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_sum']

    def get_total_sum(self, obj):
        total = obj.items.aggregate(
            total_price=Sum(F('product__price') * F('quantity'), output_field=models.DecimalField())
        )['total_price'] or Decimal('0.00')
        return total
