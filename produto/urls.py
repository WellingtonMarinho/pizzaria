from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView #ProdutoDetailView,


urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='lista-produtos'),
    path('produto/crie/', ProdutoCreateView.as_view(), name='produtos-create'),
    path('produto/edit/<int:produto_pk>', ProdutoUpdateView.as_view(), name='produtos-edit'),
    path('produto/delete/<int:produto_pk>', ProdutoDeleteView.as_view(), name='produtos-delete'),
    # path('<slug>', ProdutoDetailView.as_view(), name='produto'),

    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('categoria/crie/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/edit/<int:categoria_pk>', CategoriaUpdateView.as_view(), name='categoria-edit'),
    path('categoria/delete/<int:categoria_pk>', CategoriaDeleteView.as_view(), name='categoria-delete'),
]
