from django.urls import path
# from .views import PedidoCreateView, pedido
from .views import pedido


urlpatterns = [
    # path('pedido/create/', PedidoCreateView.as_view(), name='pedido-create'),
    path('pedido/create/', pedido, name='pedido-create'),
]
