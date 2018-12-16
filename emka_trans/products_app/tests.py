from django.test import TestCase
from products_app.models import Product


class ProductTestCase(TestCase):
    pass
    # def setUp(self):
    #     Product.objects.create(name="Jabłko",genre="Golden",name_deliver="Adma Kot",amount= 300, price=0.2)
    #     Product.objects.create(name="Gruszka",genre="Gold",name_deliver="Adma List",amount= 200, price=2)

    # def test_products_created(self):
    #     gruszka=Product.objects.get(name="Gruszka")
    #     self.assertTrue(isinstance(gruszka,Product))


class ResponseTest(TestCase):
    def test_detail(self):
        respose=self.client.get('/1/')
        self.assertEqual(respose.status_code,200)
