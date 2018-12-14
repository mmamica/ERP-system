from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)


# Create your views here.
from . import models
from order_app.models import Checkout
from products_app.models import Product 
class IndexView(TemplateView):
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        return context

class AdminCheckoutListView(ListView):
    model = Checkout
    template_name = 'admin_app/order_list.html'

class AdminCheckoutDetailView(DetailView):
    context_object_name = 'order_details'
    model=Checkout
    template_name = 'admin_app/order_detail.html'
    # un_success_url = reverse_lazy("admin_app:order_list")


    def get_queryset(self):
        return Checkout.objects.filter(name_client=self.request.user)

class AdminProductListView(ListView):
    template_name = 'admin_app/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(name_deliver=self.request.user)
