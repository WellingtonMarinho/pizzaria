from django.urls import path
# from .views import ItemPedidoCreateView
from .views import cria_pedido, lista_pedido


urlpatterns = [
    # path('pedido/create/', ItemPedidoCreateView.as_view(), name='pedido-create'),
    path('pedido/create/', cria_pedido, name='pedido-create'),
    path('pedidos/', lista_pedido, name='pedido-list'),
]
