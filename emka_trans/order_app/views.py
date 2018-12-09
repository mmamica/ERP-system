from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
import datetime


class CheckoutView(ListView):
    model = models.Checkout


class CheckoutListView(ListView):
    model = models.Checkout

    def get_queryset(self):
        return models.Checkout.objects.filter(name_client=self.request.user)


class CheckoutDetailView(DetailView):
    context_object_name = 'checkout_details'
    model=models.Checkout
    template_name = 'order_app/order_detail.html'

    def get_queryset(self):
        return models.Checkout.objects.filter(name_client=self.request.user)


class CheckoutCreateView(View):
    template_name='order_app/new_order.html'

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
        new_checkout = models.Checkout.objects.create(name_client=self.request.user, price=0, weigth=0,
                                                      route_client=False,
                                                      date=datetime.date.today(), magazine=False)
        new_checkout.save()
        order = new_checkout.id
        return redirect('order_app:detail', pk=order)


class ProductAddView(CreateView):
    fields = ("name_product", "amount")
    model = models.OrderedProducts

    def get_success_url(self):
        checkout = self.kwargs.get('pk')
        # product_name=self.object.name_product
        # #tu też powinno wyszukiwac po id a nie po name, ale najpierw trzeba pozmieniać w modelu
        # product=models.Product.objects.get(name=product_name)
        # price=product.price
        # models.Checkout.objects.filter(id=checkout).update(price=price)
        return reverse_lazy("order_app:detail",  kwargs={'pk': checkout})

    def form_valid(self, form, *args, **kwargs):
        checkout=self.kwargs.get('pk')
        form.instance.id_checkout = models.Checkout.objects.get(id=checkout)
        form.instance.route = False
        form.instance.id_route = 0
        form.instance.magazine = False

        return super(ProductAddView, self).form_valid(form)


class ConfirmCheckoutView(View):

    def get(self,request,pk):
        return render(request,'order_app/confirm_checkout.html')

    def post(self,request,pk):
        id = pk
        models.Checkout.objects.filter(id=id).update(confirmed=True)
        return redirect('order_app:list')


class CheckoutUpdateView(UpdateView):
    fields = ("name","price")
    model = models.Checkout


class ProductUpdateView(UpdateView):
    fields = ("name_product", "amount")
    model = models.OrderedProducts


class CheckoutDeleteView(DeleteView):
    context_object_name="order"
    model = models.Checkout
    success_url = reverse_lazy("order_app:list")


class OrderedProductsListView(ListView):
    context_object_name = 'orderedproducts_list'
    model = models.OrderedProducts


class OrderedProductsDetailView(DetailView):
    context_object_name = 'orderedproducts_details'
    model=models.Checkout
    template_name = 'order_app/order_detail.html'


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')