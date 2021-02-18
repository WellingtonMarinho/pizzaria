from django.contrib import admin
from pedido.models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', )
    list_display_links = ('cliente',)
    ordering = ('-created_at',)
    list_per_page = 10


admin.site.register(Pedido, PedidoAdmin)
