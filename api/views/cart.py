from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.cart import CartSerializer
from app.models import Cart


@api_view(['POST'])
def cart_detail(request):
    data = request.data
    telegram_id = data.get('telegram_id')
    cart = get_object_or_404(Cart, user__profile__telegram_id=telegram_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)
