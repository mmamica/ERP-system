from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfileInfo, User
from admin_app.models import Magazine, Truck
from accounts.forms import UserForm, UserProfileInfoForm
from django.test import Client
from django.contrib.auth.hashers import check_password

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
        self.assertRedirects(response, reverse('accounts:my_profile'), status_code=302)
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
        self.assertEqual(response.context['user'],self.user1)
        self.assertEqual(response.context['user_profile'],self.user1_info)

