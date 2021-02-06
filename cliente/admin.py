from django.contrib import admin
from .models import Endereco, Cliente


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'rua', 'bairro', 'cidade')
    list_display_links = ('rua',)
    list_per_page = 15
    # ordering = ('created_at',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rua', 'numero', 'bairro')
    list_display_links = ('nome',)
    list_per_page = 15
    ordering = ('created_at',)


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cliente, ClienteAdmin)