from app.models import Category


def get_categories(request):
    categories = Category.objects.all()
    categories.prefetch_related('subcategories')
    return {'categories': categories}
