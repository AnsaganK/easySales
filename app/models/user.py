import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone

from app.models import Cart
from app.models.base import BaseModel
from app.services.telegram_message import send_verification_code


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telegram_id = models.CharField(max_length=64, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль "{self.user.username}"'


class UserVerificationCode(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_codes')
    code = models.CharField(max_length=16)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        verbose_name = 'Код для верификации'
        verbose_name_plural = 'Коды для верификации'

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('app:verify_user', kwargs={'uuid': self.uuid})

    def save(self, *args, **kwargs):
        if not self.pk:
            send_verification_code(self)
        super().save(*args, **kwargs)

    @property
    def is_active(self):
        passed_seconds = (timezone.now() - self.created_at).seconds
        return passed_seconds < 300


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Cart.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.cart.save()
