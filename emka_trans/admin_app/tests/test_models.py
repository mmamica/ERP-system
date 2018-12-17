from django.test import  TestCase
from model_mommy import mommy
from admin_app.models import Truck,Route


class TruckTestMommy(TestCase):
    def setUp(self):
        self.truck= mommy.make(Truck)
    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.truck, Truck))


class RouteTestMommy(TestCase):
    def setUp(self):
        self.route= mommy.make(Route)
    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.route, Route))

   