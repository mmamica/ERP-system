from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck
from accounts.forms import UserForm, UserProfileInfoForm
from django.test import Client
from django.contrib.auth.hashers import check_password
from random_word import RandomWords

class RegistrationTestCase(TestCase):

    def setUp(self):
        self.user1 =User.objects.create(username="user1",first_name="Name1",last_name="Last1",
                            email="email1@g.pl",password='pass1')
        self.user1_info= UserProfileInfo.objects.create(user=self.user1,company_name="company 1",phone_number="123456789",longitude=50.064824,
                                                        latitude=19.923944,is_client=True)


        self.magazine=Magazine.objects.create(longitude=20.262038, latitude=49.819856, radius=50)


        self.truck1=Truck.objects.create(id_truck=1,capacity=100, return_date='2018-12-25',start_longitude=20.031655 , start_latitude=49.47704,
                                   end_longitude=19.964476, end_latitude=50.088287)



class RegisterViewTest(RegistrationTestCase):

    def test_unique_username(self):
        response=self.client.post(reverse('accounts:register_user'),data={'username':'user1','first_name':'Test1',
                                                                'last_name':'Test1','email':'test@g.pl','password':'pass_test',
                                                                'company_name':'TestFirma','city':'Kraków','street':'Floriańska','house_number':27})

        self.assertEqual(response.status_code, 200)
        self.failUnless(response.context['user_form'])
        self.assertFormError(response, 'user_form', field='username',
                             errors='A user with that username already exists.')

    def test_too_long_distance(self):
        response = self.client.post(reverse('accounts:register_user'), data={'username': 'test1', 'first_name': 'Test1',
                                                                             'last_name': 'Test1', 'email': 'test@g.pl',
                                                                             'password': 'pass_test', 'company_name':'TestFirma',
                                                                             'city': 'Krzeszowice', 'street': 'Krakowska',
                                                                             'house_number': 30})


        self.assertEqual(response.status_code,200)
        self.failUnless(response.context['profile_form'])
        self.failUnless(response.context['profile_form'].errors)

    def test_success(self):
        response = self.client.post(reverse('accounts:register_user'), data={'username': 'test1', 'first_name': 'Test1',
                                                                             'last_name': 'Test1', 'email': 'test@g.pl',
                                                                             'password': 'pass_test', 'company_name':'TestFirma',
                                                                             'city': 'Kraków', 'street': 'Adama Mickiewicza',
                                                                             'house_number': 30})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_user.html')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(UserProfileInfo.objects.count(),2)

    def test_get_success(self):
        response=self.client.get(reverse('accounts:register_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'accounts/register_user.html')
        self.failUnless(isinstance(response.context['user_form'],
                                   UserForm))
        self.failUnless(isinstance(response.context['profile_form'],
                                   UserProfileInfoForm))

    def test_coordinates_calcualtion(self):
        response=self.client.post(reverse('accounts:register_user'),data={'username': 'test1', 'first_name': 'Test1',
                                                                             'last_name': 'Test1', 'email': 'test@g.pl',
                                                                             'password': 'pass_test', 'company_name':'TestFirma',
                                                                             'city': 'Kraków', 'street': 'Adama Mickiewicza',
                                                                             'house_number': 30})

        created_user=User.objects.get(username='test1')
        created_profile=UserProfileInfo.objects.get(user=created_user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_user.html')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(UserProfileInfo.objects.count(), 2)
        self.assertEqual(19.92385,created_profile.longitude)
        self.assertEqual(50.06445,created_profile.latitude)


    def test_cluster_calculation(self):
        response = self.client.post(reverse('accounts:register_user'), data={'username': 'test1', 'first_name': 'Test1',
                                                                             'last_name': 'Test1', 'email': 'test@g.pl',
                                                                             'password': 'pass_test',
                                                                             'company_name': 'TestFirma',
                                                                             'city': 'Myślenice',
                                                                             'street': '3 Maja',
                                                                             'house_number': 20})
        created_user = User.objects.get(username='test1')
        created_profile = UserProfileInfo.objects.get(user=created_user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_user.html')
        self.assertEqual(self.truck1.id_truck, created_profile.id_cluster.id_truck)


class ChangePasswordViewTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", first_name="Name1", last_name="Last1",
                                         email="email1@g.pl", password='pass1')

        self.user1_info = UserProfileInfo.objects.create(user=self.user1, company_name="company 1", phone_number="123456789",
                                                    longitude=50.064824,
                                                    latitude=19.923944, is_client=True)
        self.c = Client()


    def test_password_change(self):

        login = self.c.login(username='user1', password='pass1')
        response = self.c.post(reverse('accounts:change_password'), data={'old_password':'pass1',
                                                                              'new_password1':'new_pass',
                                                                        'new_password2':'new_pass'})

        self.assertEqual(login,True)
        self.assertRedirects(response, reverse('accounts:edit_my_profile'), status_code=302)
        self.user1.refresh_from_db()
        self.assertTrue(check_password('new_pass', self.user1.password))


class MyProfileViewTest(TestCase):

    def test_get(self):
        user1 = User.objects.create_user(username="user1", first_name="Name1", last_name="Last1",
                                         email="email1@g.pl", password='pass1')

        user1_info = UserProfileInfo.objects.create(user=user1, company_name="company 1", phone_number="123456789",
                                                    longitude=50.064824,

                                                    latitude=19.923944, is_client=True)
        c = Client()

        login = c.login(username='user1', password='pass1')
        response=c.get(reverse('accounts:my_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(login)
        self.assertEqual(response.context['user'],user1)
        self.assertEqual(response.context['user_profile'],user1_info)
        self.assertEqual(response.context['user'].first_name,"Name1")
        self.assertEqual(response.context['user_profile'].company_name,"company 1")

class AuthViewTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", first_name="Name1", last_name="Last1",
                                         email="email1@g.pl", password='pass1')

        self.user1_info = UserProfileInfo.objects.create(user=self.user1, company_name="company 1", phone_number="123456789",
                                                    longitude=50.064824, latitude=19.923944, is_client=True)

        self.c = Client()

    def test_login_success(self):

        response = self.c.get(reverse('accounts:user_login'))

        self.assertEquals(response.status_code, 200)

        response=self.c.post(reverse('accounts:user_login'), data={'username':'user1','password':'pass1'})

        self.assertIn('_auth_user_id', self.c.session)
        self.assertRedirects(response,reverse('index'))

    def test_login_fail(self):
        response = self.c.get(reverse('accounts:user_login'))

        self.assertEquals(response.status_code, 200)

        response = self.c.post(reverse('accounts:user_login'), data={'username': 'user1', 'password': 'wrong_pass'})

        self.assertFormError(response, 'form',field=None,
                             errors='Błąd logowania! Spróbuj ponownie')

    def test_logout(self):
        login=self.c.login(username='user1',password='pass1')

        self.assertTrue(login)
        response = self.c.get(reverse('logout'))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response,reverse('index'))
        self.assertNotIn('_auth_user_id', self.c.session)


class ShowProfileTestView(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", first_name="Name1", last_name="Last1",
                                         email="email1@g.pl", password='pass1')

        self.user1_info = UserProfileInfo.objects.create(user=self.user1, company_name="company 1", phone_number="123456789",
                                                    longitude=50.064824, latitude=19.923944, is_client=True)

        self.c = Client()

    def test_show_profile(self):
        response=self.c.get(reverse("accounts:show_profile",  kwargs={'username': 'user1'}))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['user'], self.user1)
        self.assertEqual(response.context['user_profile'], self.user1_info)


# views (uses selenium)

class TestRegister(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestRegister, self).setUp()
        self.randomUsernameClient = RandomWords().get_random_word()
        self.randomUsernameDriver = RandomWords().get_random_word()

    def tearDown(self):
        self.selenium.quit()
        super(TestRegister, self).tearDown()

    def test_register_deliever_success(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/register_user/')

        selenium.find_element_by_id('id_username').send_keys(self.randomUsernameDriver)
        selenium.find_element_by_id('id_first_name').send_keys('testtest')
        selenium.find_element_by_id('id_last_name').send_keys('test')
        selenium.find_element_by_id('id_email').send_keys('test@g.com')
        selenium.find_element_by_id('id_password').send_keys('pass')
        selenium.find_element_by_id('id_company_name').send_keys('tmp')
        selenium.find_element_by_id('id_phone_number').send_keys('123456789')
        selenium.find_element_by_id('city').send_keys('Krakow')
        selenium.find_element_by_id('street').send_keys('al.Mickiewicza')
        selenium.find_element_by_id('house_number').send_keys('1')
        selenium.find_element_by_id('id_is_client')
        selenium.find_element_by_name('register').click()
        selenium.implicitly_wait(40)
        assert 'You have registered successfully' in selenium.page_source

    def test_register_client_success(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/register_user/')
        selenium.find_element_by_id('id_username').send_keys(
            self.randomUsernameClient)
        selenium.find_element_by_id('id_first_name').send_keys('testtest')
        selenium.find_element_by_id('id_last_name').send_keys('test')
        selenium.find_element_by_id('id_email').send_keys('test@g.com')
        selenium.find_element_by_id('id_password').send_keys('pass')
        selenium.find_element_by_id('id_company_name').send_keys('tmp')
        selenium.find_element_by_id('id_phone_number').send_keys('123456789')
        selenium.find_element_by_id('city').send_keys('Krakow')
        selenium.find_element_by_id('street').send_keys('al.Mickiewicza')
        selenium.find_element_by_id('house_number').send_keys('1')
        selenium.find_element_by_id('id_is_client').click()
        selenium.find_element_by_name('register').click()
        selenium.implicitly_wait(20)
        assert 'You have registered successfully' in selenium.page_source

class TestLogin(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestLogin, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestLogin, self).tearDown()

    def test_login_success(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        selenium.find_element_by_name('username').send_keys('testClient')
        selenium.find_element_by_name('password').send_keys('qwertyuiop')
        selenium.find_element_by_name('login').click()
        selenium.implicitly_wait(20)
        assert 'LOGOUT' in selenium.page_source

    def test_login_wrong_password_error(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        selenium.find_element_by_name('username').send_keys('testtest')
        selenium.find_element_by_name('password').send_keys('badpass')
        selenium.find_element_by_name('login').click()
        selenium.implicitly_wait(20)
        assert 'LOGIN' in selenium.page_source

    def test_login_user_not_exists_error(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        selenium.find_element_by_name('username').send_keys(
            RandomWords().get_random_word())
        selenium.find_element_by_name('password').send_keys('badpass')
        selenium.find_element_by_name('login').click()
        assert 'LOGIN' in selenium.page_source

class TestLogout(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestLogout, self).setUp()
        self.selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        self.selenium.find_element_by_name('username').send_keys('testClient')
        self.selenium.find_element_by_name('password').send_keys('qwertyuiop')
        self.selenium.find_element_by_name('login').click()

    def tearDown(self):
        self.selenium.quit()
        super(TestLogout, self).tearDown()

    def test_logout(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000')
        self.selenium.find_element_by_name('logout_nav').click()
        assert 'LOGIN' in selenium.page_source

class TestEditProfile(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestEditProfile, self).setUp()
        self.selenium.get('http://127.0.0.1:8000/accounts/user_login/')
        self.selenium.find_element_by_name('username').send_keys('Deliever')
        self.selenium.find_element_by_name('password').send_keys('qwertyuiop')
        self.selenium.find_element_by_name('login').click()

    def tearDown(self):
        self.selenium.quit()
        super(TestEditProfile, self).tearDown()

    def test_edit_profile_info_success(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/accounts/profile/edit/')
        selenium.find_element_by_id('id_first_name').send_keys('testtest')
        selenium.find_element_by_id('id_last_name').send_keys('test')
        selenium.find_element_by_id('id_company_name').send_keys('test')
        selenium.find_element_by_id('id_phone_number').send_keys('123456789')
        selenium.find_element_by_name('zapisz').click()
        assert 'My profile' in selenium.page_source

class TestButtons(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TestButtons, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestButtons, self).tearDown()

    def test_index_button(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        selenium.find_element_by_name('index').click()
        assert 'INDEX' in selenium.page_source

    def test_admin_button(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        selenium.find_element_by_name('admin').click()
        assert 'Django administration' in selenium.page_source

    def test_login_button(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        selenium.find_element_by_name('login_nav').click()
        assert 'Username:' in selenium.page_source
