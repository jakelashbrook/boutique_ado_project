from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    ''' Orders the fields in the Product Admin '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',) # to reverse stick a - infront of sku


class CategoryAdmin(admin.ModelAdmin):
    ''' Prioritises showing the friendly name in Category Admin '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
