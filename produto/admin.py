from django.contrib import admin
from .models import Sabor, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', )
    list_display_links = ('categoria',)
    ordering = ('created_at',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco')
    list_display_links = ('nome', 'categoria', 'preco')
    list_filter = ('categoria', )
    search_fields = ('nome', 'categoria')
    list_per_page = 10
    ordering = ('created_at',)

    # list_editable = ('name', 'type', 'price', 'is_active', 'uuid',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Sabor, ProdutoAdmin)