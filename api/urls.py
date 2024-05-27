from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    # User
    path('user/create', views.create_user, name='create_user'),

    # Category
    path('category', views.category_list, name='category_list'),
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('subcategory/<slug:slug>/products', views.product_list, name='product_list'),

    # Product
    path('product/<slug:slug>', views.product_detail, name='product_detail'),

    # Cart
    path('cart/add', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart_detail, name='cart_detail')
]
