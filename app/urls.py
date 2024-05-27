from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),

    # Categories
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('category/<slug:slug>/<slug:subcategory_slug>', views.subcategory_detail, name='subcategory_detail'),

    # User
    path('user', views.user_list, name='user_list'),
    path('user/sending', views.user_sending, name='user_sending'),
    path('user/check', views.check_user, name='check_user'),
    path('user/verify/<uuid:uuid>', views.verify_user, name='verify_user'),
    path('user/logout', views.logout_user, name='logout'),

    # Product
    path('cart/add', views.add_to_cart, name='add_to_cart'),

    # Cart
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/<int:product_id>/delete', views.delete_cart_item, name='delete_cart_item'),
]
