from django.test import TestCase
from django.urls import reverse,resolve

class UrlPaternTest(TestCase):
    def test_upload_xls(self):
        respose=self.client.get('/upload_xls/')
        self.assertEqual(respose.status_code,404)  
    def test_index(self):
        respose=self.client.get('/')
        self.assertEqual(respose.status_code,200)  

    # def test_detail(self):
    #     respose=self.client.get('(?P<pk>\d+))/')
    #     self.assertEqual(respose.status_code,404) 
# class UrlsTest:
#     def test_detail_url(self):
#         path=reverse('detail',kwargs={'pk':1})
#         assert resolve(path).view_name=='detail