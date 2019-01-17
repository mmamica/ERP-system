from django.test import TestCase, RequestFactory
from model_mommy import mommy
from admin_app.models import Truck, Route, Magazine


class TruckTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.truck = Truck.objects.create(id_truck=1,
                                          capacity=200,
                                          return_date='2018-01-01')

    def test__str__(self):
        self.assertEquals(self.truck.__str__(), 'Truck object (1)')

    def test_if_instatnce(self):
        self.assertTrue(isinstance(self.truck, Truck))


class RouteTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.truck = Truck.objects.create(id_truck=1,
                                          capacity=200,
                                          return_date='2018-01-01')
        self.route = Route.objects.create(id_route=1,
                                          products_list='[200,12,34,56,76]',
                                          date='2018-01-01',
                                          id_truck=self.truck
                                          )

    def test__str__(self):
        self.assertEquals(self.route.__str__(), 'Route object (1)')

    def test_if_instatnce(self):
        self.assertTrue(isinstance(self.route, Route))


class MagazineTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.magazine = Magazine.objects.create(id_magazine=1,
                                                latitude=200.5678,
                                                longitude=133.21,
                                                radius=12)

    def test__str__(self):
        self.assertEquals(self.magazine.__str__(), 'Magazine object (1)')

    def test_if_instatnce(self):
        self.assertTrue(isinstance(self.magazine, Magazine))


class TruckTestMommy(TestCase):
    def setUp(self):
        self.truck = mommy.make(Truck)

    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.truck, Truck))


class RouteTestMommy(TestCase):
    def setUp(self):
        self.route = mommy.make(Route)

    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.route, Route))


class MagazineTestMommy(TestCase):
    def setUp(self):
        self.route = mommy.make(Magazine)

    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.route, Magazine))