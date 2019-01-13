from django.test import TestCase
from model_mommy import mommy
from order_app.models import OrderedProducts
from order_app.forms import OrderedProductsForm
#from django_forms_test import field, cleaned, FormTest


class OrderedProductsFormTest(TestCase):
    def test_OrderedProductsFormT_valid(self):
        form=OrderedProductsForm(data={
            'name':"jabłko",'genre':"super",'amount':"200"})
        self.assertTrue(form.is_valid())