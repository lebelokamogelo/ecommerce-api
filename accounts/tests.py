from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json


class TestSetUp(APITestCase):
    def setUp(self):
        data = {
            "email": "test@example.com",
            "username": "test",
            "password": "1234"
        }

        response = self.client.post(reverse('register'), data)

        self.client.login(email = "test@example.com", password = "1234")
