from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from pedido.models import Pedido, ItemPedido
from pedido.forms import PedidoForm, ItemPedidoForm, FormSet
from django.urls import reverse, reverse_lazy
from django.forms.models import inlineformset_factory


def cria_pedido(request):
    if request.method == "GET":
        form = PedidoForm()
        form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)
        form_itempedido = form_item_pedido_factory()
        context = {
            'form': form,
            'formset': form_itempedido,
            'page_title': 'Lista de Pedidos'
        }
        return render(request, 'pedido/form_pedido.html', context)

    elif request.method == "POST":
        form = PedidoForm(request.POST)
        form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm)
        form_itempedido = form_item_pedido_factory(request.POST)
        if form.is_valid() and form_itempedido.is_valid():
            pedido = form.save()
            form_itempedido.instance = pedido
            form_itempedido.save()
            return redirect(reverse('core:index'))
        else:
            context = {
                'form': form,
                'formset': form_itempedido,
                'page_title': 'Pedidos'
            }
            return render(request, 'pedido/form_pedido.html', context)


def lista_pedido(request):
    if request.method == "GET":
        pedidos = Pedido.objects.all()
        context = {'obj_list': pedidos,
                   'page_title': 'Lista de Pedidos'}
        print(context['obj_list'])
        return render(request, 'pedido/list_pedido.html', context)


def edita_pedido(request, obj_pk):
    if request.method == "GET":
        pedido = Pedido.objects.get(pk=obj_pk)
        if pedido is None:
            return redirect(reverse('pedido-list'))

        form = PedidoForm(instance=pedido)
        formset = FormSet(instance=pedido)
        context = {'form': form, 'formset': formset, 'page_title': 'Lista de Pedidos'}
        return render(request, 'pedido/form_pedido.html', context)

    elif request.method == "POST":
        pedido = Pedido.objects.get(pk=obj_pk)
        if not pedido:
            return redirect(reverse('pedido-list'))
        form = PedidoForm(request.POST, instance=pedido)
        formset = FormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            objeto = form.save()
            formset.instance = objeto
            formset.save()
            return redirect(reverse('core:index'))
        else:
            context = {'form': form, 'formset': formset, 'page_title': 'Lista de Pedidos'}
            return render(request, 'pedido/form_pedido.html', context)


def detalha_pedido(request, obj_pk):
    if request.method == "GET":
        pedido = Pedido.objects.get(pk=obj_pk)
        item_pedido = pedido.itempedido_set.all()
        #pedido = ItemPedido.objects.filter(pedido.pk=obj_pk)
        # pedido = get_object_or_404(Pedido, pk=obj_pk)
        context = {'obj': item_pedido}
        return render(request, 'pedido/detail_pedido.html', context)



# class ItemPedidoCreateView(CreateView):
#     form_class = PedidoForm
#     template_name = 'pedido/form_pedido.html'
#     # success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super(ItemPedidoCreateView, self).get_context_data(**kwargs)
#         context['forms'], context['formset'] = PedidoForm(), ItemPedidoForm()
#         context['page_title'] = 'Pedido'
#         if self.request.POST:
#             context['forms'] = PedidoForm(self.request.POST)
#             context['formset'] = ItemPedidoForm(self.request.POST)
#
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         forms, formset = context['form'], context['formset']
#         if forms.is_valid and formset.is_valid():
#             self.object = form.save()
#             forms.instance = self.object
#             formset.instance = self.object
#             forms.save()
#             formset.save()
#             return redirect('core:index')
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
