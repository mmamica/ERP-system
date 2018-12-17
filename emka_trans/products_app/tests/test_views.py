from django.test import TestCase
from django.urls import reverse,resolve



class ProductListView(TestCase):
    def test_list_view_displays_form_for_existing_lists(self):
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertIsInstance(response.context['form'], ExistingListItemForm)

