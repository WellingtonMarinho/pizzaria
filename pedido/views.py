from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from pedido.models import Pedido, ItemPedido
from pedido.forms import PedidoForm, ItemPedidoForm, formset
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
    form_class = PedidoForm
    template_name = 'pedido/form_pedido.html'
    # success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ItemPedidoCreateView, self).get_context_data(**kwargs)
        context['forms'], context['formset'] = PedidoForm(), ItemPedidoForm()
        context['page_title'] = 'Pedido'
        if self.request.POST:
            context['forms'] = PedidoForm(self.request.POST)
            context['formset'] = ItemPedidoForm(self.request.POST)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forms, formset = context['form'], context['formset']
        print(form)
        print()
        print(dir(form))
        print()
        print(forms, "======FORMS=======")
        print()
        print(formset, "======FORMSET=======")

        if forms.is_valid and formset.is_valid():
            self.object = form.save()
            forms.instance = self.object
            formset.instance = self.object
            forms.save()
            formset.save()
            return redirect('core:index')
        else:
            return self.render_to_response(self.get_context_data(form=form))