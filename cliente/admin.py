from django.contrib import admin
from .models import Endereco, Cliente


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'cidade')
    list_display_links = ('rua',)
    list_per_page = 15

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rua', 'numero', 'bairro')
    list_display_links = ('nome',)
    list_per_page = 15

admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cliente, ClienteAdmin)