from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.user import UserSerializer
from app.forms.user import UserCreateForm


@api_view(['POST'])
def create_user(request):
    telegram_id = request.data.get('telegram_id')

    if telegram_id and User.objects.filter(profile__telegram_id=telegram_id).exists():
        user = User.objects.get(profile__telegram_id=telegram_id)
        serializer = UserSerializer(user, data=request.data)
    else:
        serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        profile = user.profile
        profile.telegram_id = telegram_id
        profile.save()
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def create_user(request):
#     telegram_id = request.POST.get('telegram_id')
#     if telegram_id and User.objects.filter(profile__telegram_id=telegram_id).exists():
#         form = UserCreateForm(request.POST, instance=User.objects.get(profile__telegram_id=telegram_id))
#         if form.is_valid():
#             form.save()
#
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             profile = user.profile
#             profile.telegram_id = telegram_id
#             profile.save()
#             return JsonResponse({
#                 'message': 'User created'
#             }, status=200)
#         else:
#             print(form.errors)
#     return JsonResponse({
#         'message': 'Please enter valid data'
#     }, status=400)
