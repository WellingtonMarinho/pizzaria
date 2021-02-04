from django.contrib import admin
from .models import Product #, Type

# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('type',)
#     list_display_links = ('type',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'is_active')
    list_display_links = ('name', 'type', 'price')
    list_filter = ('type', )
    search_fields = ('name', 'type')
    list_per_page = 25
    # list_editable = ('name', 'type', 'price', 'is_active', 'uuid',)

# admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)