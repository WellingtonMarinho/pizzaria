from django.shortcuts import render, redirect
from django.views.generic import CreateView
from pedido.models import Pedido, ItemPedido
from pedido.forms import PedidoForm, ItemPedidoForm
from django.urls import reverse, reverse_lazy
from django.forms.models import inlineformset_factory

#
# def pedido(request):
#     if request.method == "GET":
#         form = PedidoForm()
#         form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)
#         form_itempedido = form_item_pedido_factory()
#         context = {
#             'form': form,
#             'form_itempedido': form_itempedido,
#         }
#         return render(request, 'pedido/form_pedido.html', context)
#
#     elif request.method == "POST":
#         form = PedidoForm(request.POST)
#         form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm)
#         form_itempedido = form_item_pedido_factory(request.POST)
#         if form.is_valid() and form_itempedido.is_valid():
#             pedido = form.save()
#             form_itempedido.instance = pedido
#             form_itempedido.save()
#             return redirect(reverse('core:index'))
#         else:
#             context = {
#                 'form': form,
#                 'form_itempedido': form_itempedido
#             }
#             return render(request, 'pedido/form_pedido.html', context)


class ItemPedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/form_pedido.html'
    success_url = reverse_lazy('index')
    object = None

    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)
        form_item_pedido = item_pedido_factory()
        return self.render_to_response(
            self.get_context_data(form=form, form_itempedido=form_item_pedido))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_item_pedido_factory = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm)
        form_itempedido = form_item_pedido_factory(self.request.POST)
        if form.is_valid() and form_itempedido.is_valid():
            return self.form_valid(form, form_itempedido)
        else:
            return self.form_invalid(form, form_itempedido)

    def form_valid(self, form, inline_formset_factory):
        self.object = form.save(commit=False)
        self.object.save()
        form_itempedido = inline_formset_factory.save(commit=False)
        for each in form_itempedido:
            each.save()
        return redirect(reverse('core:index'))

    def form_invalid(self, form, inline_formset_factory):
        return self.render_to_response(
            self.get_context_data(form=form, form_itempedido=inline_formset_factory))