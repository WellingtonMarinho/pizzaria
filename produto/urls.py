from django.urls import path
from .views import ProdutoListView, ProdutoCreateView,  \
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView #ProdutoDetailView,



urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista_produtos'),
    path('crie-produto/', ProdutoCreateView.as_view(), name='produtos_create'),
    path('edit-produto/<int:produto_pk>', ProdutoCreateView.as_view(), name='produtos_create'),
    # path('<slug>', ProdutoDetailView.as_view(), name='produto'),

    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('categoria/edit-categoria/<int:categoria_pk>', CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('categoria/crie-categorias/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:categoria_pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),

]