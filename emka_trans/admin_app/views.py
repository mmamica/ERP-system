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
from django.http import HttpResponse, HttpResponseForbidden
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required



@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(),name='dispatch')
class IndexView(TemplateView):
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(),name='dispatch')
class AdminCheckoutListView(ListView):
    model = Checkout
    template_name = 'admin_app/order_list.html'

    def get_queryset(self):
        return Checkout.objects.filter(confirmed=True)

@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(),name='dispatch')
class AdminCheckoutDetailView(DetailView):
    context_object_name = 'order_details'
    model=Checkout
    template_name = 'admin_app/order_detail.html'
    # un_success_url = reverse_lazy("admin_app:order_list")


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(),name='dispatch')
class AdminProductListView(ListView):
    template_name = 'admin_app/product_list.html'
    model=Product



def VRP():
    print('Kupaa')
