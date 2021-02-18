from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Cliente, Endereco
from .forms import ClienteForm, EnderecoForm


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/clientes.html'
    paginate_by = 10
    context_object_name = 'obj_list' # altera o nome da váriavel de contexto que por default é 'object'_list

    # É necessário rescrever esses dois métodos para aplicar
    # Variáveis de contexto, como título, nome específico para tags e etc.
    def get_queryset(self):
        queryset = Cliente.objects.all().order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Clientes'
        context['list_title'] = 'Lista de Clientes'
        context['editable'] = True
        context['back_link'] = reverse_lazy('index')
        context['back_button'] = 'Voltar'
        context['home'] = 'Index'
        return context


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'forms.html'
    success_url = reverse_lazy('clientes')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'forms.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')
    pk_url_kwarg = 'cliente_pk'


class ClienteDeleteView(DeleteView):
    model = Cliente
    pk_url_kwarg = 'cliente_pk'
    success_url = reverse_lazy('clientes')
    template_name = 'delete.html'
