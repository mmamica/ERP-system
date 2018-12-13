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
    template_name = 'admin_app/orders_list.html'

def my_view(request):
    # View code here...
    return render(request, 'adminapp/admin_app_index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')