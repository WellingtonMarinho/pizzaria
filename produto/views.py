from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Produto
from .forms import ProdutoForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/lista-produto.html'
    paginate_by = 10


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/cria-produto.html'
    success_url = reverse_lazy('cria-produtos') # Define que url será apontada após o save()

    # def get_success_url(self):
    #     return reverse('cria-produtos')