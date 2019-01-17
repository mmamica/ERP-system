from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck
from accounts.forms import UserForm, UserProfileInfoForm
from django.test import Client
from django.test import TestCase
from order_app.models import Checkout, OrderedProducts
from products_app.models import Product

class ProductAppTestCase(TestCase):
    def setUp(self):
        self.deliver=User.objects.create_user(username="deliver", first_name="Name1", last_name="Last1",
                                              email="email1@g.pl", password='pass1')

        self.deliver_info = UserProfileInfo.objects.create(user=self.deliver, company_name="company 1",
                                                         phone_number="123456789",
                                                         longitude=50.064824, latitude=19.923944, is_client=False)

        self.deliver2 = User.objects.create_user(username="deliver2", first_name="Name1", last_name="Last1",
                                                email="email1@g.pl", password='pass1')

        self.deliver2_info = UserProfileInfo.objects.create(user=self.deliver2, company_name="company 1",
                                                           phone_number="123456789",
                                                           longitude=50.064824, latitude=19.923944, is_client=False)

        self.product1=Product.objects.create(name='prod1',genre='gat1',name_deliver=self.deliver,amount=100,price=10)
        self.product2=Product.objects.create(name='prod2',genre='gat2',name_deliver=self.deliver,amount=200,price=20)
        self.product3=Product.objects.create(name='prod3',genre='gat2',name_deliver=self.deliver2,amount=300,price=30)

        self.c = Client()

class ProductListViewTest(ProductAppTestCase):

    def test_product_list_get(self):
        self.c.login(username='deliver',password='pass1')
        response=self.c.get(reverse('products_app:list'))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'products_app/product_list.html')
        self.assertEqual(len(response.context['product_list']),2)


class ProductDetailViewTest(ProductAppTestCase):
    def test_product_detail_get(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:detail',kwargs={'pk':self.product1.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_app/product_detail.html')
        self.assertEqual(response.context['product_details'].id,self.product1.id)

    def test_product_detail_wrong_owner(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:detail', kwargs={'pk': self.product3.id}))
        self.assertEqual(response.status_code, 403)

class ProductCreateViewTest(ProductAppTestCase):

    def test_create_product_get(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:create'))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'products_app/product_form.html')

    def test_create_product_post(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.post(reverse('products_app:create'),data={'name':'new_product','genre':'new_genre',
                                                                    'price':15,'amount':150,'weight':10})

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('products_app:list'))
        self.assertEqual(Product.objects.count(),4)
        created=Product.objects.latest('id')
        self.assertEqual(created.name_deliver,self.deliver)

class ProductUpdateViewTest(ProductAppTestCase):
    def test_update_product_get(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:update',kwargs={'pk':self.product1.id}))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'products_app/product_form.html')

    def test_update_product_wrong_owner(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:update', kwargs={'pk': self.product3.id}))

        self.assertEqual(response.status_code, 403)

    def test_update_product_post(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.post(reverse('products_app:update', kwargs={'pk': self.product1.id}),data={'name':'new_name',
                                                                                                     'genre':'new_genre',
                                                                                                     'price':15,'amount':150,
                                                                                                     'weight':10})

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('products_app:list'))
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.name,'new_name')
        self.assertEqual(self.product1.genre,'new_genre')
        self.assertEqual(self.product1.price,15)
        self.assertEqual(self.product1.amount,150)
        self.assertEqual(self.product1.name_deliver,self.deliver)


class ProductDeleteViewTest(ProductAppTestCase):
    def test_product_delete_get(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:delete', kwargs={'pk': self.product1.id}))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'products_app/product_confirm_delete.html')

    def test_product_delete_wrong_owner(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:delete', kwargs={'pk': self.product3.id}))

        self.assertEqual(response.status_code, 403)

    def test_product_delete_post(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.post(reverse('products_app:delete', kwargs={'pk': self.product1.id}))

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('products_app:list'))
        self.assertEqual(Product.objects.count(),2)

class UploadXlsViewTest(ProductAppTestCase):
    def test_upload_xls_get(self):
        self.c.login(username='deliver', password='pass1')
        response = self.c.get(reverse('products_app:xls'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_app/xls.html')

    def test_upload_xls_get_not_logged_in(self):

        response = self.c.get(reverse('products_app:xls'),follow=True)

        self.assertEqual(response.status_code, 404)

    def test_upload_xls_post(self):
        self.c.login(username='deliver', password='pass1')

        with open('/home/agnieszka/emka_trans/ERP-system/emka_trans/products_app/tests/test.xlsx','rb') as fp:
            response=self.c.post(reverse('products_app:xls'), data={ 'excel_file': fp})

        self.assertEqual(response.status_code,200)
        self.assertEqual(Product.objects.count(),6)
        self.assertEqual(Product.objects.latest('id').name,"C")
        self.assertEqual(Product.objects.get(id=5).genre,"b")
        self.assertEqual(Product.objects.get(id=4).price,1)

    def test_upload_xls_update(self):
        self.c.login(username='deliver', password='pass1')

        with open('/home/agnieszka/emka_trans/ERP-system/emka_trans/products_app/tests/test_update.xlsx','rb') as fp:
            response=self.c.post(reverse('products_app:xls'), data={ 'excel_file': fp})

        self.assertEqual(response.status_code,200)
        self.assertEqual(Product.objects.count(),3)
        self.assertEqual(Product.objects.get(name='prod1').price,30)
        self.assertEqual(Product.objects.get(name='prod1').amount, 10)
        self.assertEqual(Product.objects.get(name='prod2').amount, 20)
        self.assertEqual(Product.objects.get(name='prod2').price, 40)