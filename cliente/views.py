from django.views.generic import ListView
from .models import Cliente, Endereco
from django.urls import reverse_lazy


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente-list.html'



class ClienteCreateView():
    pass