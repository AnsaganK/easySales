from django.shortcuts import get_object_or_404, render, aget_object_or_404

from app.models import Category, Product, SubCategory


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategories.all().order_by('created_at')
    products = Product.objects.filter(subcategory__category=category).order_by('created_at')
    return render(request, 'app/product/list.html', {
        'category': category,
        'subcategories': subcategories,
        'products': products
    })


def subcategory_detail(request, slug, subcategory_slug):
    selected_subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    subcategories = SubCategory.objects.filter(category=selected_subcategory.category).order_by('created_at')
    products = Product.objects.filter(subcategory=selected_subcategory).order_by('created_at')
    return render(request, 'app/product/list.html', {
        'selected_subcategory': selected_subcategory,
        'category': selected_subcategory.category,
        'subcategories': subcategories,
        'products': products
    })
