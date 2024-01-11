from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestHome(APITestCase):

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
