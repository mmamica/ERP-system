from django.test import TestCase
from model_mommy import mommy
from order_app.models import OrderedProducts
from order_app.forms import OrderedProductsForm
from django_forms_test import field, cleaned, FormTest


class OrderedProductsFormTest(TestCase):
    def test_OrderedProductsFormT_valid(self):
        form=OrderedProductsForm(data={
               'iquery':"5",
            'iquery_choices':"5",
            'iquery2':"6",
            'iquery_choices2':"6",
            'genre':"6",
            'name':"Jabłko",'genre':"Golden",'amount':"200"})
        self.assertTrue(form.is_valid())
    

