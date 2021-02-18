from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView #ProdutoDetailView,


urlpatterns = [
    path('produtos/', ProdutoListView, name='lista-produtos'),
    path('produto/crie/', ProdutoCreateView, name='produtos-create'),
    path('produto/edit/<int:produto_pk>', ProdutoUpdateView, name='produtos-edit'),
    path('produto/delete/<int:produto_pk>', ProdutoDeleteView, name='produtos-delete'),
    path('produtos/combos/', ProdutoListView, name='lista-combos'),
    # path('<slug>', ProdutoDetailView.as_view(), name='produto'),

    path('categorias/', CategoriaListView, name='categorias'),
    path('categoria/crie/', CategoriaCreateView, name='categoria-create'),
    path('categoria/edit/<int:categoria_pk>', CategoriaUpdateView, name='categoria-edit'),
    path('categoria/delete/<int:categoria_pk>', CategoriaDeleteView, name='categoria-delete'),
]
