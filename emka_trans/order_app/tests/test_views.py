from django.test import TestCase


class UrlPaternTest(TestCase):
    def test_create(self):
        respose=self.client.get('/create/')
        self.assertEqual(respose.status_code,404)  
    def test_index(self):
        respose=self.client.get('/')
        self.assertEqual(respose.status_code,404)  
    def test_ajax(self):
        respose=self.client.get('ajax/load_genres/')
        self.assertEqual(respose.status_code,404)  
    # def test_detail(self):
    #     respose=self.client.get('(?P<pk>\d+))/')
    #     self.assertEqual(respose.status_code,404) 
