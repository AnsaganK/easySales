from django.db import models
from django.shortcuts import reverse
from pytils.translit import slugify

from app.models.base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='category_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:subcategory_detail', kwargs={'slug': self.category.slug, 'subcategory_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
