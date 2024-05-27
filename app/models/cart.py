from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F

from app.models.base import BaseModel
from app.models.product import Product


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя "{self.user.get_full_name()}"'

    def get_total_price(self):
        total = self.items.aggregate(
            total_price=Sum(F('product__price') * F('quantity'), output_field=models.DecimalField())
        )['total_price'] or Decimal('0.00')
        return total


class CartItem(BaseModel):
    class ViaChoices(models.TextChoices):
        SITE = 'site', 'Сайт'
        TELEGRAM = 'telegram', 'Телеграм'

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(default=1)
    via = models.CharField(max_length=64, choices=ViaChoices.choices, default=ViaChoices.SITE)
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f'Продукт из корзины #{self.cart.id}'

    @property
    def get_sum(self):
        return self.product.price * self.quantity
