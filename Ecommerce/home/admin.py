from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category')
    raw_id_fields = ('category',)
    
