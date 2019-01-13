from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from . import models
import openpyxl
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductListView(ListView):
    """
    Display a list of products :model:`products_app.Product`.

    **Template:**
    
    :template:`products_app/product_list.html`
    """
    template_name = 'products_app/product_list.html'

    def get_queryset(self):
        """
        Return the list of items for this view.
        """
        return models.Product.objects.filter(name_deliver=self.request.user)

class ProductDetailView(DetailView):
    """
    Detail information about object :model:`products_app.Product`.

    ``Product``
        An instance of :model:`products_app.Product`.

    **Template:**
    
    :template:`products_app/product_detail.html`
    """

    context_object_name = 'product_details'
    model = models.Product
    template_name = 'products_app/product_detail.html'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        try:
            models.Product.objects.get(id=pk, name_deliver=user)
            return super(ProductDetailView, self).dispatch(request, *args, **kwargs)
        except models.Product.DoesNotExist:
            return HttpResponseForbidden()

class ProductCreateView(CreateView):
    """
    View for creating a new object, with a response rendered by a template :model:`products_app.Product`.
    
    ``Product``
        An instance of :model:`products_app.Product`.

    **Template:**
    
    :template:`products_app/product_list.html`
    """
    fields = ("name","genre","price","amount","weight")
    model = models.Product
    success_url = reverse_lazy("products_app:list")

    def form_valid(self, form):
        """If the form is valid, save the associated model. Default value of deliever"""
        form.instance.name_deliver = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(UpdateView):
    """
    View for updating an object, with a response rendered by a template. :model:`products_app.Product`.
    
    ``Product``
        An instance of :model:`products_app.Product`.

    **Template:**
    
    :template:`products_app/product_list.html`
    """

    fields = ("name","genre","amount","price","weight")
    model = models.Product
    success_url = reverse_lazy("products_app:list")

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # example
        user = request.user  # Take user from request

        try:
            models.Product.objects.get(id=pk, name_deliver=user)
            return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)
        except models.Product.DoesNotExist:
            return HttpResponseForbidden()


class ProductDeleteView(DeleteView):
    """
    View for deleting an object retrieved with self.get_object(), with a 
    response rendered by a template.

    ``Product``
        :model:`products_app.Product`.
    """

    model = models.Product
    success_url = reverse_lazy("products_app:list")

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # example
        user = request.user 

        try:
            models.Product.objects.get(id=pk, name_deliver=user)
            return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
        except models.Product.DoesNotExist:
            return HttpResponseForbidden()

@method_decorator(login_required, name='dispatch')
class UploadXlsView(View):
    """
    View for uploading an excel file.

    **Template:**
    
    :template:`products_app/xls.html`
    """

    template_name = 'products_app/xls.html'

    def get(self,request):
        return render(request, self.template_name, {})

    def post(self,request):
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)
        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        first_row = worksheet[1]
        name=0
        genre=0
        amount=0
        price=0
        weight=0
        it=0

        for cell in first_row:
            title=str(cell.value)
            if title.lower() == 'nazwa':
                name=it
            elif title.lower() == 'gatunek':
                genre=it
            elif title.lower() == 'cena':
                price=it
            elif title.lower() == 'ilość':
                amount=it
            elif title.lower() == 'waga':
                weight=it
            it = it + 1
        success=False
        i=0
        for row in worksheet.iter_rows():
            i=i+1
            if i==1:
                continue
            else:
                existing_product=models.Product.objects.filter(name=str(row[name].value),
                                                               genre=str(row[genre].value), name_deliver=request.user).count()
                if existing_product==0:
                    new_product=models.Product.objects.create(name=str(row[name].value), genre=str(row[genre].value),
                                                name_deliver=request.user, amount=int(str(row[amount].value)),
                                                price=int(str(row[price].value)),weight=int(str(row[weight].value)))
                    new_product.save()
                    success=True
                else:
                    models.Product.objects.filter(name=str(row[name].value), genre=str(row[genre].value),
                                                  name_deliver=request.user).update(amount=int(str(row[amount].value)),
                                                price=int(str(row[price].value)),weight=int(str(row[weight].value)))
                    success = True
        return render(request, self.template_name , {'success':success})
