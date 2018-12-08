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
        context['injectme'] = "Checkout"
        return context

class CheckoutView(ListView):
    model = models.Checkout

class CheckoutListView(ListView):
    model = models.Checkout

class CheckoutDetailView(DetailView):
    context_object_name = 'checkout_details'
    model=models.Checkout
    template_name = 'order_app/order_detail.html'


class CheckoutCreateView(CreateView):
    fields = ("id_checkout","name_client","price","weigth","route_client","date","magazine")
    model = models.Checkout
    success_url = reverse_lazy("order_app:list")

class CheckoutUpdateView(UpdateView):
    fields = ("name","price")
    model = models.Checkout

class CheckoutDeleteView(DeleteView):
    model = models.Checkout
    success_url = reverse_lazy("order_app:list")

class OrderedProductsListView(ListView):
    context_object_name = 'orderedproducts_list'
    model = models.OrderedProducts

class COrderedProductsLView(DetailView):
    context_object_name = 'orderedproducts_details'
    model=models.Checkout
    template_name = 'order_app/order_detail.html'



class OrderDetailView(DetailView):
    context_object_name = 'order_details'
    model = models.Order
    template_name = 'order_app/order_detail.html'



class OrderListView(ListView):
    model = models.Order

# class OrderCreateView(CreateView):
#     fields = ("name","genre","id_client","amount",)
#     model = models.Order


class OrderUpdateView(UpdateView):
    fields = ("name","price")
    model = models.Order

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy("order_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')