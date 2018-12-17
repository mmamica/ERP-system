from django.test import  TestCase
from model_mommy import mommy
from  order_app.models import Checkout,OrderedProducts


class CheckoutTestMommy(TestCase):
    def setUp(self):
        self.checkout= mommy.make(Checkout)
    def test_checkout_creation_mommy(self):
        self.assertTrue(isinstance(self.checkout, Checkout))
    def test__str__mommy(self):
        self.assertEqual(self.checkout.__str__(), str(self.checkout.id))


class OrderedProductsTestMommy(TestCase):
    def setUp(self):
        self.orderedProducts= mommy.make(OrderedProducts)
    def test_orderedProducts_creation_mommy(self):
        self.assertTrue(isinstance(self.orderedProducts, OrderedProducts))
    def test__str__mommy(self):
        self.assertEqual(self.orderedProducts.__str__(), self.orderedProducts.name_product.name)
    
   