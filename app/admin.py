from django.contrib import admin
from .models import Profile, Cart, CartItem, Product, Category, SubCategory
from .models.user import UserVerificationCode


#
#               Cart Admin
#

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']


#
#               Category Admin
#
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['category']


#
#               Product Admin
#
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


#
#               User Admin
#
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(UserVerificationCode)
class UserVerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created_at']
