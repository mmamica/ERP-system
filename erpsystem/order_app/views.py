from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Orders"
        return context
class OrderListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'Order_list'

    # Example of making your own:
    # context_object_name = 'Orders'
    model = models.Order


class OrderDetailView(DetailView):
    context_object_name = 'order_details'
    model = models.Order
    template_name = 'order_app/order_detail.html'


class OrderCreateView(CreateView):
    fields = ("name","genre","id_client","amount",)
    model = models.Order


class OrderUpdateView(UpdateView):
    fields = ("name","price")
    model = models.Order

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy("order_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
