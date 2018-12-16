from django.test import TestCase
from accounts.models import UserProfileInfo

class UserProfileInfoTest(TestCase):
     def test_string_representation(self):
        company_name =UserProfileInfo(company_name="AGH")
        self.assertEqual(str(company_name),company_name.company_name)



