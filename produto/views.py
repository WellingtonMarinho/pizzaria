from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, RedirectView
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produtos.html'
    paginate_by = 10
    ordering = ('-created_at')


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/cria-produto.html'
    success_url = reverse_lazy('lista-produtos') # Define que url será apontada após o save()


# class ProdutoDetailView(DetailView):
#     model = Produto
#     template_name = 'produto/cria-produto.html'
#     pk_url_kwarg = 'slug'

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto/cria-produto.html'
    form_class = ProdutoForm
    success_url = 'lista-produtos'
    pk_url_kwarg = 'produto_pk'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produto/categorias.html'
    paginate_by = 10
    ordering = ('-created_at')


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produto/cria-categoria.html'
    success_url = reverse_lazy('categorias')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'produto/cria-categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias')
    pk_url_kwarg = 'categoria_pk'


class CategoriaDeleteView(DeleteView):
    model = Categoria
    pk_url_kwarg = 'categoria_pk'
    success_url = 'categorias'
    template_name = 'produto/cria-categoria.html'

#
# class CategoriaDeleteView(RedirectView):
#
#     pk_url_kwarg = 'categoria_pk'
#
#     def get_reditect_url(self, *args, **kwargs):
#         categoria = Categoria.objects.get(pk=kwargs['categoria_pk'])
#         categoria.delete()
#         self.url = reverse_lazy('categorias')
#         return super(CategoriaDeleteView, self).get_redirect_url(*args, **kwargs)
