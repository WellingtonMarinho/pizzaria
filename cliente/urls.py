from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('clientes/', ClienteListView, name='clientes'),
    path('cliente/crie/', ClienteCreateView, name='cliente-cria'),
    path('cliente/edit/<int:cliente_pk>', ClienteUpdateView, name='cliente-edit'),
    path('cliente/delete/<int:cliente_pk>', ClienteDeleteView, name='cliente-delete'),
]
