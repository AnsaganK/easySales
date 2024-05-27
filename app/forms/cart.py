from django import forms

from app.models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
