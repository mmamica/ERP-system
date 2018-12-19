from django.test import RequestFactory, TestCase
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User
from admin_app.models import Truck
from model_mommy import mommy

class UserProfileInfoTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@g.com', password='top_secret')
        self.truck=Truck.objects.create(id_truck=1,
                                        capacity=200,
                                        return_date='2018-01-01')
        self.adam=UserProfileInfo.objects.create(user=self.user,
                                                company_name="AGA",
                                                phone_number="123456789",
                                                longitude=1.200,
                                                latitude=51.23,
                                                is_client=True,
                                                id_cluster=self.truck)
    def test__str__(self):
        self.assertEquals(self.adam.__str__(),'jacob')
    def test_if_instatnce(self):
        self.assertTrue(isinstance(self.adam,UserProfileInfo))

class UserProfileInfoTestMommy(TestCase):
    def setUp(self):
        self.user= mommy.make(UserProfileInfo)
    def test_user_creation_mommy(self):
        self.assertTrue(isinstance(self.user, UserProfileInfo))
    def test__str__mommy(self):
        self.assertEqual(self.user.__str__(), self.user.user.username)