from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Cliente, Endereco
from .forms import ClienteForm, EnderecoForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente-list.html'
    paginate_by = 10
    ordering = '-created_at'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cria-cliente.html'
    success_url = reverse_lazy('')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = ''
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')
    pk_url_kwarg = 'cliente_pk'


class ClienteDeleteView(DeleteView):
    model = Cliente
    pk_url_kwarg = 'cliente_pk'
    success_url = reverse_lazy('clientes')
    template_name = 'delete.html'