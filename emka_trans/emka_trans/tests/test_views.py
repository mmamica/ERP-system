from django.test import TestCase


class AdminPaternTest(TestCase):
    def test_admin(self):
        respose=self.client.get('/admin/')
        self.assertEqual(respose.status_code,302)  
    def test_admin_app(self):
        respose=self.client.get('admin_app/')
        self.assertEqual(respose.status_code,200)  
    def test_index(self):
        respose=self.client.get('/')
        self.assertEqual(respose.status_code,200) 
    def test_accounts(self):
        respose=self.client.get('accounts/')
        self.assertEqual(respose.status_code,404)
    def test_logout(self):
        respose=self.client.get('/logout/')
        self.assertEqual(respose.status_code,200) 
    def test_user(self):
        respose=self.client.get('/user/')
        self.assertEqual(respose.status_code,302) 
    def test_orders(self):
        respose=self.client.get('/orders/')
        self.assertEqual(respose.status_code,302) 
        # self.assertTemplateUsed(response, 'about.html')
    def test_products(self):
        respose=self.client.get('/products/')
        self.assertEqual(respose.status_code,404)