from django.db import models
from pytils.translit import slugify

from app.models.category import SubCategory
from app.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    subcategory = models.ForeignKey(
        SubCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='products'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
