from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck
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