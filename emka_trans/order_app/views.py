from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from accounts.models import UserProfileInfo
from products_app.models import Product
from . import forms
from django.forms import ValidationError
from django.http import Http404
import datetime


class CheckoutView(ListView):
    model = models.Checkout

@method_decorator(login_required, name='dispatch')
class CheckoutListView(ListView):
    """
        Displays a list of checkouts :model:`order_app.Checkout`.

        **Template:**

        :template:`order_app/checkout_list.html`
    """
    model = models.Checkout

    def get_queryset(self):
        return models.Checkout.objects.filter(name_client=self.request.user)

@method_decorator(login_required, name='dispatch')
class CheckoutDetailView(DetailView):
    """
        Displays checkout details :model:`order_app.Checkout`.

        **Template:**
        :template:`order_app/order_detail.html`
    """
    context_object_name = 'checkout_details'
    model=models.Checkout
    template_name = 'order_app/order_detail.html'

    def get_queryset(self):
        return models.Checkout.objects.filter(name_client=self.request.user)

@method_decorator(login_required, name='dispatch')
class CheckoutCreateView(CreateView):
    """
        Allows the user to create a new order :model:`order_app.Checkout`.

        **Template:**
        :template:`order_app/checkout_form.html`
    """
    form_class = forms.CheckoutCreateForm
    model=models.Checkout

    def get(self, *args, **kwargs):
        all_dates=models.Checkout.objects.all().values_list('date', flat=True)
        dates_list=[]
        for date in all_dates:
            checkouts = models.Checkout.objects.filter(date=date)
            times = checkouts.count()
            if (times >= 3):
                dates_list.append(date)

        dates=list(set(dates_list))
        return render(self.request, 'order_app/checkout_form.html',{'form':self.form_class,'unavailable_dates':dates})

    def get_success_url(self):
        checkout = self.object.id
        print(checkout)
        return reverse_lazy("order_app:detail",  kwargs={'pk': checkout})

    def form_valid(self, form, *args, **kwargs):
        form.instance.name_client=self.request.user
        form.instance.price=0
        form.instance.weigth=0
        form.instance.route_client=False
        form.instance.magazine = False

        return super(CheckoutCreateView, self).form_valid(form)


class ProductAddView(CreateView):
    """
        Allows the user to add a new product to the order :model:`order_app:OrderedProducts`.

        **Template:**
        :template:`order_app/orderedproducts_form.html`
    """
    form_class = forms.OrderedProductsForm
    model = models.OrderedProducts

    def get(self, *args, **kwargs):
        self.form_class=forms.OrderedProductsForm(user=self.request.user, ajax=False)
        return render(self.request, 'order_app/orderedproducts_form.html',{'form':self.form_class})

    def get_success_url(self):
        checkout = self.kwargs.get('pk')
        product_name=self.object.name_product
        product=models.Product.objects.get(id=product_name.id)
        old_price=models.Checkout.objects.get(id=checkout)
        old_weight=models.Checkout.objects.get(id=checkout).weigth
        price=(product.price*self.object.amount)+old_price.price
        weight=(self.object.amount)+old_weight
        models.Checkout.objects.filter(id=checkout).update(price=price,weigth=weight)
        return reverse_lazy("order_app:detail",  kwargs={'pk': checkout})

    def form_valid(self, form, *args, **kwargs):
        checkout = self.kwargs.get('pk')
        cluster = UserProfileInfo.objects.get(user=self.request.user).id_cluster
        delivers = UserProfileInfo.objects.filter(id_cluster=cluster, is_client=False)
        for deliver in delivers:
            check_product=models.Product.objects.filter(name=form.cleaned_data['name'], genre=form.cleaned_data['genre'],
                                                     name_deliver=deliver.user).count()
            if check_product!=0:
                prod=models.Product.objects.get(name=form.cleaned_data['name'], genre=form.cleaned_data['genre'],
                                                     name_deliver=deliver.user)
        form.instance.name_product=prod
        message=None
        if (form.cleaned_data['amount'] > prod.amount):
             #form.add_error('amount', 'Ilość produktu niedostępna!')
             self.form_class = forms.OrderedProductsForm(user=self.request.user, ajax=False)
             message="Ilość produktu niedostępna!"
             return render(self.request, template_name='order_app/orderedproducts_form.html',
                           context={'form': self.form_class,'message':message})
        form.instance.id_checkout = models.Checkout.objects.get(id=checkout)
        form.instance.route = False
        form.instance.id_route = 0
        form.instance.magazine = False
        form.instance.name_deliver=prod.name_deliver

        return super(ProductAddView, self).form_valid(form)


class ConfirmCheckoutView(View):
    """
        Allows the user to confirm the order.
        Confirmed orders can not be edited.
        If the amount of ordered products is not available, the user can edit or delete the order.

        **Template:**
        :template:`order_app/confirm_checkout.html`
        :template:`order_app/checkout_list.html`

    """
    def get(self,request,pk):
        if  models.Checkout.objects.filter(id=pk):
            return render(request,'order_app/confirm_checkout.html')
        else:
            raise Http404

    def post(self,request,pk):
        id = pk
        missing_products=[]
        enough=True
        products=models.OrderedProducts.objects.filter(id_checkout=id)
        for product in products:
            prod=product.name_product
            base_amount=prod.amount
            if (base_amount<product.amount):
                enough=False
                missing_products.append(prod)

        if enough:
            models.Checkout.objects.filter(id=id).update(confirmed=True)

            for product in products:
                old_amount= models.Product.objects.get(id=product.name_product.id).amount
                new_amount=old_amount-product.amount
                models.Product.objects.filter(id=product.name_product.id).update(amount=new_amount)

            return redirect('order_app:list')
        else:
            return render(request, 'order_app/confirm_checkout.html',context={'missing_products':missing_products, 'checkout':id})

def load_genres(request):
    """
        Loads genres based on the selected product.

    :param request: HttpRequest
    :return: HttpResponse

    """
    product = request.GET.get('product')
    cluster = UserProfileInfo.objects.get(user=request.user).id_cluster
    delivers = UserProfileInfo.objects.filter(id_cluster=cluster, is_client=False)
    #deliver = delivers.user.username
    genres=[]
    for deliver in delivers:
        name=deliver.user
        genres = genres+list(models.Product.objects.filter(name=product, name_deliver=name).order_by('name'))
    return render(request, 'order_app/genres_dropdown_list_options.html', {'genres': genres})


class CheckoutUpdateView(UpdateView):
    fields = ("name","price")
    model = models.Checkout

class ProductUpdateView(UpdateView):
    """
        Allows the user to update the amount of the selected product :model:`order_app.OrderedProducts`.

        **Template:**
        :template:`order_app:orderedproducts_form.html`
        :template:`order_app:order_detail.html`

    """
    fields = ("amount",)
    model = models.OrderedProducts

    def get_success_url(self):
        product_name = self.object.name_product
        checkout = self.object.id_checkout
        product = models.Product.objects.get(id=product_name.id)
        old_price = models.Checkout.objects.get(id=checkout.id)
        old_weight=models.Checkout.objects.get(id=checkout.id).weigth
        price = (product.price * self.object.amount) + old_price.price
        weight = (self.object.amount) + old_weight
        models.Checkout.objects.filter(id=checkout.id).update(price=price,weigth=weight)
        return reverse_lazy("order_app:detail", kwargs={'pk': checkout})

    def form_valid(self, form, *args, **kwargs):
        product_name = self.object.name_product
        checkout = self.object.id_checkout
        product = models.Product.objects.get(id=product_name.id)
        old_price = models.Checkout.objects.get(id=checkout.id)
        old_weight=models.Checkout.objects.get(id=checkout.id).weigth
        old_amount=models.OrderedProducts.objects.get(id_checkout=checkout.id,id=self.object.id)
        if (form.cleaned_data['amount'] > product.amount):
            form.add_error('amount','Ilość produktu niedostępna!')
            return render(self.request,template_name='order_app/orderedproducts_form.html',context={'form':form})
        price = old_price.price-(product.price * old_amount.amount)
        weight=old_weight-old_amount.amount
        models.Checkout.objects.filter(id=checkout.id).update(price=price,weigth=weight)
        return super(ProductUpdateView, self).form_valid(form)

class ProductDeleteView(DeleteView):

    """
        Allows the user to delete product from order.
        **Context**
        `order`
            An instance of :model:`order_app.Product`
        **Template:**
        :template:`order_app/orderedproducts_confirm_delete.html`
        :template:`order_app/order_detail.html`
    """
    context_object_name = "order"
    model = models.OrderedProducts

    def get_success_url(self):
        product_name = self.object.name_product
        checkout = self.object.id_checkout
        product = models.Product.objects.get(id=product_name.id)
        old_price = models.Checkout.objects.get(id=checkout.id)
        old_weight=models.Checkout.objects.get(id=checkout.id).weigth
        price = old_price.price - (product.price * self.object.amount)
        weight=old_weight-(self.object.amount)
        models.Checkout.objects.filter(id=checkout.id).update(price=price,weigth=weight)
        return reverse_lazy("order_app:detail", kwargs={'pk': checkout})

class CheckoutDeleteView(DeleteView):
    """
        Allows the user to delete order.

        **Context**
        `order`
            An instance of :model:`order_app.Checkout`
        **Template:**
        :template:`order_app/checkout_confirm_delete.html`
        :template:`order_app/checkout_list.html`
    """
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

class AllProductsView(View):
    """
        Allows the user browse available products.

        **Context**
        `products`
            A list of :model:`order_app.OrderedProducts`.

        **Template:**
        :template:`order_app/all_products_list.html`
    """
    def get(self,request):
        user=self.request.user
        cluster=UserProfileInfo.objects.get(user=user).id_cluster
        delivers=UserProfileInfo.objects.filter(id_cluster=cluster, is_client=False)
        products=[]
        for deliver in delivers:
            products=products+(list(Product.objects.filter(name_deliver=deliver.user)))
        return render(request,'order_app/all_products_list.html',{'product_list':products})

