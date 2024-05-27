from django.shortcuts import get_object_or_404, render, aget_object_or_404

from app.models import Category, Product, SubCategory


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategories.all().order_by('created_at')
    products = Product.objects.filter(subcategory__category=category).order_by('created_at')
    return render(request, 'app/category/detail.html', {
        'category': category,
        'subcategories': subcategories,
        'products': products
    })


def subcategory_detail(request, slug, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    return render(request, 'app/subcategory/detail.html', {
        'subcategory': subcategory,
    })
