from django.contrib import admin
from .models import Produto #, Type

# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('type',)
#     list_display_links = ('type',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'preco')
    list_display_links = ('nome', 'tipo', 'preco')
    list_filter = ('tipo', )
    search_fields = ('nome', 'tipo')
    list_per_page = 25
    # list_editable = ('name', 'type', 'price', 'is_active', 'uuid',)

# admin.site.register(Type, TypeAdmin)
admin.site.register(Produto, ProdutoAdmin)