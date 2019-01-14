from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck, Route
from accounts.forms import UserForm, UserProfileInfoForm
from django.test import Client
from django.test import TestCase
from order_app.models import Checkout, OrderedProducts
from products_app.models import Product



class AdminAppTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", first_name="Name1", last_name="Last1",
                                              email="email1@g.pl", password='pass1')

        self.user1_info = UserProfileInfo.objects.create(user=self.user1, company_name="company 1",
                                                         phone_number="123456789",
                                                         longitude=50.064824, latitude=19.923944, is_client=True)

        self.user2= User.objects.create_user(username="user2", first_name="Name1", last_name="Last1",
                                              email="email1@g.pl", password='pass1')

        self.user2_info = UserProfileInfo.objects.create(user=self.user2, company_name="company 1",
                                                         phone_number="123456789",
                                                         longitude=50.064824, latitude=19.923944, is_client=True)

        self.checkout=Checkout.objects.create(name_client=self.user1,price=0,weigth=150,route_client=False,
                                              date='2018-12-20',hour=1,magazine=False,confirmed=False)

        self.checkout2=Checkout.objects.create(name_client=self.user2,price=200,weigth=50,route_client=False,
                                              date='2018-12-25',hour=2,magazine=False,confirmed=False)

        self.checkout3 = Checkout.objects.create(name_client=self.user1, price=200, weigth=50, route_client=False,
                                                 date='2018-12-25', hour=2, magazine=False, confirmed=False)

        self.admin=User.objects.create_user(username='admin', first_name='Admin',last_name='Admin', email='admin@g.pl',
                                            password='admin',is_staff=True, is_superuser=True)

        self.checkout = Checkout.objects.create(name_client=self.user1, price=0, weigth=150, route_client=False,
                                                date='2018-12-20', hour=1, magazine=False, confirmed=True)

        self.user3 = User.objects.create_user(username="user3", first_name="Name1", last_name="Last1",
                                              email="email1@g.pl", password='pass1')

        self.user3_info = UserProfileInfo.objects.create(user=self.user3, company_name="company 1",
                                                         phone_number="123456789",
                                                         longitude=50.064824, latitude=19.923944, is_client=False)

        self.product = Product.objects.create(name='jabłko', genre='nwm', name_deliver=self.user3, amount=100, price=10)

        self.ordered_product = OrderedProducts.objects.create(id_checkout=self.checkout, name_deliver=self.user3,
                                                              name_product=self.product, amount=20, route=False,
                                                              id_route=0, magazine=False)

        self.c = Client()

        self.magazine = Magazine.objects.create(id_magazine=1,
                                                latitude=200.5678,
                                                longitude=133.21,
                                                radius=12)

        self.truck = Truck.objects.create(id_truck=1,
                                          capacity=200,
                                          return_date='2018-01-01')

        self.route = Route.objects.create(id_route=1,
                                          products_list='[200,12,34,56,76]',
                                          date='2018-01-01',
                                          id_truck=self.truck
                                          )

        self.route2 = Route.objects.create(id_route=2,
                                          products_list='[200,14,4,56,76]',
                                          date='2018-01-01',
                                          id_truck=self.truck
                                          )
        self.c = Client()


class AdminCheckoutListViewTest(AdminAppTestCase):
    def test_list_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:order_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_app/order_list.html')
        self.assertEqual(len(response.context['checkout_list']),1)

    def test_list_not_confirmed(self):
        self.checkout2 = Checkout.objects.create(name_client=self.user1, price=0, weigth=150, route_client=False,
                                                date='2018-12-20', hour=1, magazine=False, confirmed=False)
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:order_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_app/order_list.html')
        self.assertEqual(len(response.context['checkout_list']), 1)

    def test_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:order_list'))

        self.assertEqual(response.status_code, 302)

class AdminCheckoutDetailViewTest(AdminAppTestCase):
    def test_detail_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:order_detail', kwargs={'pk':self.checkout.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['order_details'].id,self.checkout.id)

    def test_detail_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:order_detail', kwargs={'pk': self.checkout.id}))

        self.assertEqual(response.status_code, 302)

class AdminProductListViewTest(AdminAppTestCase):
    def test_product_list_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:product_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['product_list']),1)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:product_list'))

        self.assertEqual(response.status_code, 302)


class IndexView20Test(AdminAppTestCase):
    def test_index_view20_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index20'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']),1)
        self.assertEqual(len(response.context['routes_tomorrow']),0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index20'))

        self.assertEqual(response.status_code, 302)

    def test_algorithm(self):
        self.c.login(username='admin', password='admin')
        response = self.c.post(reverse('admin_app:index20'), data={'date': '2018-12-18', 'claster': '1'})


class IndexView21Test(AdminAppTestCase):
    def test_index_view20_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index21'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']),1)
        self.assertEqual(len(response.context['routes_tomorrow']),0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index21'))

        self.assertEqual(response.status_code, 302)

class IndexView22Test(AdminAppTestCase):
    def test_index_view20_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index22'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']),1)
        self.assertEqual(len(response.context['routes_tomorrow']),0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index22'))

        self.assertEqual(response.status_code, 302)


class IndexView23Test(AdminAppTestCase):
    def test_index_view20_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index23'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']), 1)
        self.assertEqual(len(response.context['routes_tomorrow']), 0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index23'))

        self.assertEqual(response.status_code, 302)


class IndexViewTest(AdminAppTestCase):
    def test_index_view20_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']), 1)
        self.assertEqual(len(response.context['routes_today']), 0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index'))

        self.assertEqual(response.status_code, 302)


class IndexView1Test(AdminAppTestCase):
    def test_index_view1_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index1'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']), 1)
        self.assertEqual(len(response.context['routes_today']), 0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index1'))

        self.assertEqual(response.status_code, 302)


class IndexView2Test(AdminAppTestCase):
    def test_index_view1_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index2'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']), 1)
        self.assertEqual(len(response.context['routes_today']), 0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index2'))

        self.assertEqual(response.status_code, 302)


class IndexView3Test(AdminAppTestCase):
    def test_index_view1_get(self):
        self.c.login(username='admin', password='admin')
        response = self.c.get(reverse('admin_app:index3'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['trucks']), 1)
        self.assertEqual(len(response.context['routes_today']), 0)

    def test_product_list_not_superuser(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('admin_app:index3'))

        self.assertEqual(response.status_code, 302)