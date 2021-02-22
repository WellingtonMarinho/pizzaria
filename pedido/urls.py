from django.urls import path
from .views import ItemPedidoCreateView
# from .views import pedido


urlpatterns = [
    path('pedido/create/', ItemPedidoCreateView.as_view(), name='pedido-create'),
    # path('pedido/create/', pedido, name='pedido-create'),
]
