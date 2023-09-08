from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUserModel
# Create your tests here.


class AccountTest(TestCase):
    username = 'test username'
    password = 'test password'
    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = CustomUserModel.objects.create_user(username='amir', password='123')

    def test_sign_up_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_form(self):
        get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
