from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='clientes-list'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/edit/<int:obj_pk>', ClienteUpdateView.as_view(), name='cliente-edit'),
    path('cliente/delete/<int:obj_pk>', ClienteDeleteView.as_view(), name='cliente-delete'),
]
