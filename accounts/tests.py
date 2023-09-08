from django.test import TestCase
from django.urls import reverse

from .models import CustomUserModel
# Create your tests here.


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUserModel.objects.create_user(username='amir', password='123')

    def test_sign_up_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)