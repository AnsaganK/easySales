from rest_framework import serializers

from app.models import Product, SubCategory, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
