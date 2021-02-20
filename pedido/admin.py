from django.contrib import admin
from pedido.models import Pedido, ItemPedido


class ItemPedidoAdmin(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {
    #     'fields': (
    #         'uuid',
    #         'is_active',
    #         # 'created_at',
    #         # 'modified_at',
    #     )
    # }),
    #  ('Pedido', {
    #      'fields': ('cliente', 'endereco')
    #  }
    #
    #   )
    #  )
    inlines = [ItemPedidoAdmin]
    # readonly_fields = ['uuid', 'created_at']

#     list_display = ('id', 'cliente', )
#     list_display_links = ('cliente',)
#     ordering = ('-created_at',)
#     list_per_page = 10
#
#
# class ItemPedidoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'pedido', 'produto', 'quantidade', 'preco')
#     list_display_links = ('id', 'pedido', 'produto')


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
