from django.urls import reverse
from rest_framework.test import APITestCase

from .models import User


class TestSetUp(APITestCase):
    def setUp(self):
        data = {
            "email": "test@example.com",
            "username": "test",
            "password": "1234"
        }

        self.client.post(reverse('register'), data)

        self.client.login(email="test@example.com", password="1234")

    def test_model(self):
        self.assertEqual(str(User.objects.first()), "test")
