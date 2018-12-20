from django.test import TestCase
from accounts.forms import (UserForm,
                            UserProfileInfoForm,
                            EditUserProfileForm,
                            LoginForm)
from model_mommy import mommy
from django.contrib.auth.models import User
import tempfile
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfileInfo
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate
#from emka_trans.settings import AUTH_TEMPLATES
#from django_forms_test import field, cleaned, FormTest

#from django.test import LiveServerTestCase
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


class TestDataMixin:
    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create_user(username='testclient', password='password', email='testclient@example.com')


class UserFormTest(TestCase):
    def setUp(self):
        self.user = mommy.make(User)

    def test_UserForm_valid(self):
        form = UserForm(
            data={'username': "ela", 'first_name': "krzz", 'last_name': self.user.last_name, 'email': self.user.email,
                  'password': self.user.password})
        self.assertTrue(form.is_valid())

    def test_UserForm_username_exists(self):
        form = UserForm(
            data={'username': self.user.username, 'first_name': self.user.first_name, 'last_name': self.user.last_name,
                  'email': self.user.email, 'password': self.user.password})
        self.assertFalse(form.is_valid())

    def test_UserForm_blank_invalid(self):
        form = UserForm(data={'username': "", 'first_name': "", 'email': "", 'password': ""})
        self.assertFalse(form.is_valid())

    def test_UserForm_blank_username(self):
        form = UserForm(data={'username': "", 'first_name': self.user.first_name, 'last_name': self.user.last_name,
                              'email': self.user.email, 'password': self.user.password})
        self.assertFalse(form.is_valid())

    def test_UserForm_blank_first_name(self):
        form = UserForm(
            data={'username': "elaaa", 'first_name': "", 'last_name': self.user.last_name, 'email': self.user.email,
                  'password': self.user.password})
        self.assertTrue(form.is_valid())

    def test_UserForm_blank_last_name(self):
        form = UserForm(data={'username': "elaaa", 'first_name': "tmp", 'last_name': "", 'email': self.user.email,
                              'password': self.user.password})
        self.assertTrue(form.is_valid())

    def test_UserForm_blank_email(self):
        form = UserForm(data={'username': "elaaa", 'first_name': "tmp", 'last_name': self.user.last_name, 'email': "",
                              'password': self.user.password})
        self.assertTrue(form.is_valid())

    def test_UserForm_blank_passwoard(self):
        form = UserForm(
            data={'username': "elaaa", 'first_name': "tmp", 'last_name': self.user.last_name, 'email': self.user.email,
                  'password': ""})
        self.assertFalse(form.is_valid())


class UserProfileInfoFormTest(TestCase):
    def steUp(self):
        self.image = tempfile.NamedTemporaryFile(suffix=".jpg").name

    def test_UserProfileInfoForm_valid(self):
        form = UserProfileInfoForm(data={'company_name': "AGH",
                                         'phone_number': 123456789,
                                         'city': "Kraków",
                                         'street': "Mickiewicz",
                                         'house_number': 2,
                                         'profile_pic': "",
                                         'is_client': "1"})
        self.assertTrue(form.is_valid())


class EditUserProfileFormTest(TestDataMixin, TestCase):
    def setUp(self):
        self.user = mommy.make(User)

    def test_username_validity(self):
        user = self.user
        data = {'username': 'not valid'}
        form = UserChangeForm(data, instance=user)
        self.assertFalse(form.is_valid())
        validator = next(v for v in User._meta.get_field('username').validators if v.code == 'invalid')
        self.assertEqual(form["username"].errors, [str(validator.message)])


class LoginFormTest(TestDataMixin, TestCase):
    def test_invalid_username(self):
        data = {
            'username': 'jsmith_does_not_exist',
            'password': 'test123',
        }
        form = LoginForm(None, data)
        self.assertFalse(form.is_valid())

    def test_valid_username(self):
        data = {
            'username': 'testclient',
            'password': 'password',
        }
        form = LoginForm(data)
        self.assertTrue(form.is_valid())

        #  SELENIUM
        #
        # class UserFormTestCase(LiveServerTestCase):
        #
        #     def setUp(self):
        #         self.selenium = webdriver.Firefox()
        #         super(UserFormTestCase, self).setUp()
        #
        #     def tearDown(self):
        #         self.selenium.quit()
        #         super(UserFormTestCase, self).tearDown()
