from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class PagesTest(TestCase):

    def test_home_view_url(self):
        response = self.client.get('')
        response_name = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_name.status_code, 200)