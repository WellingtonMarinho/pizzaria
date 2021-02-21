from django.contrib import admin
from pedido.models import Pedido, ItemPedido


class ItemPedidoAdmin(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    exclude = ('is_active', )
    inlines = [ItemPedidoAdmin]


admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(ItemPedido)
