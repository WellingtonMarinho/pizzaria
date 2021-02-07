from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='clientes'),
    path('clientes/crie/', ClienteCreateView.as_view(), name='cliente-cria'),
    path('clientes/edit/<int:cliente_pk>', ClienteUpdateView.as_view(), name='cliente-edit'),
    path('clientes/delete/<int:cliente_pk>', ClienteDeleteView.as_view(), name='cliente-delete'),

]