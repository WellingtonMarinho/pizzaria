from django.urls import path
from .views import ProdutoListView, ProdutoCreateView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista-produtos'),
    path('crie/', ProdutoCreateView.as_view(), name='cria-produtos'),

]