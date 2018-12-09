from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from . import models
import openpyxl


#przeglądanie własnych produktów
class ProductListView(ListView):
    template_name = 'products_app/product_list.html'

    def get_queryset(self):
        return models.Product.objects.filter(name_deliver=self.request.user)


class ProductDetailView(DetailView):
    context_object_name = 'product_details'
    model = models.Product
    template_name = 'products_app/product_detail.html'


class ProductCreateView(CreateView):
    fields = ("name","genre","price","amount")
    model = models.Product
    success_url = reverse_lazy("products_app:list")


    #domyślna wartość dostwacy
    def form_valid(self, form):
        form.instance.name_deliver = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(UpdateView):
    fields = ("name","genre","amount","price")
    model = models.Product
    success_url = reverse_lazy("products_app:list")

    #można updateować tylko swoje produkty
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # example
        # Take user from request
        user = request.user

        try:
            models.Product.objects.get(id=pk, name_deliver=user)
            return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)
        except models.Product.DoesNotExist:
            return HttpResponseForbidden()


class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy("products_app:list")

    #można usuwać product tylko należący do cb
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # example
        # Take user from request
        user = request.user

        try:
            models.Product.objects.get(id=pk, name_deliver=user)
            return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
        except models.Product.DoesNotExist:
            return HttpResponseForbidden()


class UploadXlsView(View):
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
            it = it + 1

        i=0
        for row in worksheet.iter_rows():
            i=i+1
            if i==1:
                continue
            else:

                new_product=new_product=models.Product.objects.create(name=str(row[name].value), genre=str(row[genre].value),
                                                name_deliver=request.user, amount=int(str(row[amount].value)),
                                                price=int(str(row[price].value)))
                new_product.save()
                success=True

        return render(request, self.template_name , {'success':success})


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')