from django.urls import path
from .views import ClienteListView, ClienteCreateView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='clientes'),

]