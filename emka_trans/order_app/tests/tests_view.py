from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck
from accounts.forms import UserForm, UserProfileInfoForm
from django.test import Client
from django.test import TestCase
from order_app.models import Checkout, OrderedProducts
from products_app.models import Product
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from django.test import LiveServerTestCase
import random

class OrderAppTestCase(TestCase):
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
                                              date='2020-12-20',hour=1,magazine=False,confirmed=False)

        self.checkout2=Checkout.objects.create(name_client=self.user2,price=200,weigth=50,route_client=False,
                                              date='2020-12-25',hour=2,magazine=False,confirmed=False)

        self.user3 = User.objects.create_user(username="user3", first_name="Name1", last_name="Last1",
                                              email="email1@g.pl", password='pass1')

        self.user3_info = UserProfileInfo.objects.create(user=self.user3, company_name="company 1",
                                                         phone_number="123456789",
                                                         longitude=50.064824, latitude=19.923944, is_client=False)

        self.product=Product.objects.create(name='jabłko',genre='nwm',name_deliver=self.user3,amount=100,price=10)

        self.checkout3 = Checkout.objects.create(name_client=self.user1, price=200, weigth=50, route_client=False,
                                                 date='2020-12-25', hour=2, magazine=False, confirmed=False)

        self.ordered_product = OrderedProducts.objects.create(id_checkout=self.checkout3, name_deliver=self.user3,
                                                              name_product=self.product, amount=20, route=False,
                                                              id_route=0, magazine=False)

        self.c = Client()

class CheckoutListViewTest(OrderAppTestCase):
    def test_list_view(self):

        self.c.login(username='user1',password='pass1')
        response=self.c.get(reverse('order_app:list'))

        self.assertEqual(response.status_code,200)
        self.assertEqual(list(response.context['checkout_list']),[self.checkout, self.checkout3])

    def test_list_not_logged(self):
        response = self.c.get(reverse('order_app:list'))
        self.assertEqual(response.status_code, 302)


class CheckoutDetailViewTest(OrderAppTestCase):
    def test_detail_view(self):
        self.c.login(username='user1', password='pass1')

        response=self.c.get(reverse('order_app:detail',kwargs={'pk':1}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['checkout_details'], self.checkout)
        self.assertEqual(response.context['checkout_details'].name_client,self.checkout.name_client)

    def test_detail_not_logged(self):
        response = self.c.get(reverse('order_app:detail',kwargs={'pk':2}))
        self.assertEqual(response.status_code, 302)

    def test_detail_wrong_owner(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('order_app:detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 404)

class CheckoutCreateViewTest(OrderAppTestCase):

    def test_create_checkout_success(self):

        self.c.login(username='user1', password='pass1')
        #res=self.c.post(reverse('order_app:create'))

        response=self.c.post(reverse('order_app:create'),data={'date':'2020-12-25','hour':'1'})

        new_checkout=Checkout.objects.latest('id')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,reverse('order_app:detail',kwargs={'pk':new_checkout.id}))
        self.assertEqual(new_checkout.name_client,self.user1)
        self.assertEqual(Checkout.objects.count(),4)


    def test_create_checkout_too_many_orders(self):
        self.checkout3=Checkout.objects.create(name_client=self.user2,price=200,weigth=50,route_client=False,
                                              date='2018-12-25',hour=2,magazine=False,confirmed=False)

        self.checkout4=Checkout.objects.create(name_client=self.user2,price=200,weigth=50,route_client=False,
                                              date='2018-12-25',hour=2,magazine=False,confirmed=False)

        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:create'), data={'date': '2018-12-25', 'hour': '3'})

        self.assertEqual(response.status_code,200)
        self.assertFormError(response,'form',field='date',errors='The limit for this day is over.')

    def test_create_checkout_old_date(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:create'), data={'date': '2017-12-25', 'hour': '3'})

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', field='date', errors='Choose future date.')

    def test_create_checkout_no_free_slot(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:create'), data={'date': '2020-12-25', 'hour': '2'})

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', field='hour', errors='This slot is already taken.')

class ProductAddViewTest(OrderAppTestCase):

    def product_add_test(self):
        #product=Product.objects.get(id=1)
        self.c.login(username='user1', password='pass1')
        response=self.c.post(reverse('order_app:add_product', kwargs={'pk':self.checkout.id}),data={'amount':200,
                                                                                                    'name': self.product.name,
                                                                                                    'genre':self.product.genre})



        ordered=OrderedProducts.objects.latest('id')
        self.assertEqual(response.status_code,302)
        self.assertEqual(ordered.id_checkout.id,1)
        self.assertEqual(OrderedProducts.objects.count(),1)
        self.assertEqual(ordered.name_product,self.product)
        self.checkout.refresh_from_db()
        new_price=self.checkout.price
        self.assertEqual(new_price,200*self.product.price)



class DeleteCheckoutViewTest(OrderAppTestCase):

    def test_get(self):
        self.c.login(username='user1', password='pass1')
        response=self.c.get(reverse('order_app:delete',kwargs={'pk':self.checkout.id}))

        self.assertEqual(response.status_code,200)

    def test_confirm_delete(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:delete', kwargs={'pk': self.checkout.id}))

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('order_app:list'))
        self.assertEqual(Checkout.objects.count(),2)


class ConfirmCheckoutViewTest(OrderAppTestCase):

    def test_confirm_checkout_get(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('order_app:confirm', kwargs={'pk': self.checkout.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'order_app/confirm_checkout.html')

    def test_confirm_checkout_bad_id(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('order_app:confirm', kwargs={'pk': 5}))
        self.assertEqual(response.status_code, 404)

    def test_confirm_checkout_post(self):

        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:confirm', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('order_app:list'))
        self.checkout.refresh_from_db()
        self.assertEqual(self.checkout.confirmed, True)


class ProductUpdateViewTest(OrderAppTestCase):

    def test_product_update_get(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('order_app:update_product', kwargs={'pk': self.ordered_product.id}))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'order_app/orderedproducts_form.html')

    def test_product_update_post(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:update_product', kwargs={'pk': self.ordered_product.id}),data={'amount':10})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('order_app:detail',kwargs={'pk':self.checkout3.id}))

    def test_product_price_change(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:update_product', kwargs={'pk': self.ordered_product.id}),
                               data={'amount': 10})
        self.assertEqual(response.status_code, 302)
        self.checkout3.refresh_from_db()
        self.assertEqual(self.checkout3.price, self.product.price*10)

class ProductDeleteViewTest(OrderAppTestCase):

    def test_product_delete_get(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.get(reverse('order_app:delete_product', kwargs={'pk': self.ordered_product.id}))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'order_app/orderedproducts_confirm_delete.html')

    def test_product_delete_post(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:delete_product', kwargs={'pk': self.ordered_product.id}))

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('order_app:detail',kwargs={'pk':self.checkout3.id}))
        self.assertEqual(OrderedProducts.objects.count(),0)

    def test_product_delete_update_price(self):
        self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('order_app:delete_product', kwargs={'pk': self.ordered_product.id}))

        self.checkout3.refresh_from_db()
        self.assertEqual(self.checkout3.price,0)


# views (uses selenium)
class LoginSetUp(TestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        self.selenium.find_element_by_name('username').send_keys('Client')
        self.selenium.find_element_by_name('password').send_keys('qwertyuiop')
        self.selenium.find_element_by_name('login').click()

class TestAddOrder(LiveServerTestCase, LoginSetUp):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestAddOrder, self).tearDown()

    def test_add_order(self):
        selenium=self.selenium
        date = str(random.randint(1, 12))+'/'+str(random.randint(1, 30))+'/2019'
        selenium.get('http://127.0.0.1:8000/orders/create')
        selenium.find_element_by_name('date').send_keys(date)
        selenium.find_element_by_id(
            'id_hour').send_keys(random.randint(1, 24))
        submit=selenium.find_element_by_id('submit_btn').click()
        assert 'Product' in selenium.page_source


class TestOrderDetail(LiveServerTestCase, LoginSetUp):
    def setUp(self):
       
        super().setUp()
        date = str(random.randint(1, 12))+'/' + \
            str(random.randint(1, 30))+'/2019'
        self.selenium.get('http://127.0.0.1:8000/orders/create')
        self.selenium.find_element_by_name('date').send_keys(date)
        self.selenium.find_element_by_id(
            'id_hour').send_keys(random.randint(1, 24))
        self.selenium.find_element_by_id('submit_btn').click()

    def tearDown(self):
        self.selenium.quit()
        super(TestOrderDetail, self).tearDown()

    def test_add_product(self):
        selenium = self.selenium
        selenium.get(selenium.current_url)
        selenium.find_element_by_name('add_product').click()
        selenium.find_element_by_id('id_name').send_keys('Apple')
        selenium.find_element_by_id('id_genre').send_keys('golden')
        selenium.find_element_by_id('id_amount').send_keys('1')
        selenium.find_element_by_name('submit').click()
        assert 'Product' in selenium.page_source

    def test_confirm(self):
        selenium = self.selenium
        selenium.get(selenium.current_url)
        selenium.find_element_by_name('confirm').click()
        selenium.implicitly_wait(10)
        selenium.find_element_by_name('confirm').click()
        assert 'Your orders' in selenium.page_source

    def test_delete_delete(self):
        selenium = self.selenium
        selenium.get(selenium.current_url)
        selenium.find_element_by_name('delete_order').click()
        selenium.implicitly_wait(10)
        selenium.find_element_by_name('delete').click()
        assert 'Your orders' in selenium.page_source

    def test_delete_cancel(self):
        selenium = self.selenium
        selenium.get(selenium.current_url)
        selenium.find_element_by_name('delete_order').click()
        selenium.implicitly_wait(10)
        selenium.find_element_by_name('cancel').click()
        assert 'details:' in selenium.page_source
