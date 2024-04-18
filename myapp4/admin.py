from django.contrib import admin
from .models import Category, Product


@admin.action(description='Удалить продукты из категории')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание продукта (description)'
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# Register your models here.
