from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)


# Create your views here.
from . import models

class IndexView(TemplateView):
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        return context

class AdminCheckoutListView(ListView):
    pass
    # model = models.Checkout