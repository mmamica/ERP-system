from django.test import TestCase


class UrlPaternTest(TestCase):
    def test_register_user(self):
        respose=self.client.get('/register_user/')
        self.assertEqual(respose.status_code,404)  
    def test_user_login(self):
        respose=self.client.get('user_login/')
        self.assertEqual(respose.status_code,404)  
    def test_profile(self):
        respose=self.client.get('profile/')
        self.assertEqual(respose.status_code,404) 
    def test_profile_edit(self):
        respose=self.client.get('profile/edit/')
        self.assertEqual(respose.status_code,404)
    def test_profile_password(self):
        respose=self.client.get('/profile/password/')
        self.assertEqual(respose.status_code,404) 
