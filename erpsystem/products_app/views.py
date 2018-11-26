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
        context['injectme'] = "products"
        return context
class ProductListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'product_list'

    # Example of making your own:
    # context_object_name = 'Products'
    model = models.Product


class ProductDetailView(DetailView):
    context_object_name = 'product_details'
    model = models.Product
    template_name = 'products_app/product_detail.html'


class ProductCreateView(CreateView):
    fields = ("name","genre","id_deliever","price","amount")
    model = models.Product


class ProductUpdateView(UpdateView):
    fields = ("name","genre","amount","price")
    model = models.Product
    success_url = reverse_lazy("products_app:list")

class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy("products_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
