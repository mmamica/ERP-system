from django.test import TestCase
from products_app.models import Product
from model_mommy import mommy



class ProductTestMommy(TestCase):
    def setUp(self):
        self.product= mommy.make(Product)
    def test_checkout_creation_mommy(self):
        self.assertTrue(isinstance(self.product, Product))
    def test__str__mommy(self):
        self.assertEqual(self.product.__str__(),self.product.name)
