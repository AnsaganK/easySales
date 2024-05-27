import random

from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, reverse, render

from app.forms.user import UserCheckForm, UserVerifyForm
from app.models.user import UserVerificationCode
from app.services.telegram_message import send_message


@login_required()
def user_list(request):
    users = User.objects.all()
    return render(request, 'app/user/list.html', {
        'users': users
    })


@login_required()
def user_sending(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user_ids = request.POST.getlist('user')
        users = User.objects.filter(id__in=user_ids)
        chat_ids = users.exclude(profile__telegram_id=None).exclude(profile__telegram_id='').values_list(
            'profile__telegram_id', flat=True
        )
        send_message(chat_ids, message)
        messages.success(request, f'Отправлено {len(chat_ids)} из {users.count()}')
        return redirect(reverse('app:user_sending'))
    users = User.objects.all()
    return render(request, 'app/user/sending.html', {
        'users': users
    })


def check_user(request):
    if request.method == 'POST':
        form = UserCheckForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
                verification_code = UserVerificationCode.objects.create(
                    user=user,
                    code=''.join(random.sample('0123456789', 6))
                )
                verification_code.save()
                return redirect(verification_code.get_absolute_url())
            except User.DoesNotExist:
                messages.warning(request, 'Данный ник не зарегистрирован в базе')
                return redirect(reverse('app:check_user'))
        else:
            print(form.errors)
        return redirect(reverse('app:home'))
    return render(request, 'app/user/check.html')


def verify_user(request, uuid):
    user_verification_code = get_object_or_404(UserVerificationCode, uuid=uuid)
    if request.method == 'POST':
        form = UserVerifyForm(request.POST)
        if form.is_valid():
            if not user_verification_code.is_active:
                messages.error(request, 'Срок действия кода истек')
            elif form.cleaned_data['code'] != user_verification_code.code:
                messages.error(request, 'Неправильный код, попробуйте снова')
            else:
                login(request, user_verification_code.user)
                messages.success(request, 'Вход выполнен успешно')
                return redirect(reverse('app:home'))
        else:
            print(form.errors)
        return redirect(user_verification_code.get_absolute_url())
    return render(request, 'app/user/verify.html', {})


@login_required()
def logout_user(request):
    logout(request)
    return redirect(reverse('app:home'))
