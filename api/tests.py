from django.urls import reverse
from rest_framework import status

from accounts.tests import TestSetUp
from products.models import Categorie


class CategoryTestCase(TestSetUp):

    def test_login(self):
        response = self.client.post(reverse('login'),
                                    {"email": "test@example.co",
                                     "password": "1234"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token(self):
        response = self.client.post(reverse('token_obtain_pair'),
                                    data={"email": "test@example.com",
                                          "password": "1234"})
        # self.assertEqual(response.status_code,
        # status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_get(self):
        response = self.client.get(reverse('category'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_category_post(self):
        data = {
            'name': 'adidas'
        }

        response = self.client.post(reverse('category'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_update(self):
        self.test_category_post()
        data = {'name': "hemisphere"}

        response = self.client.put(reverse('category_read_update',
                                           kwargs={'name': 'adidas'}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('category_read_update',
                                           kwargs={'name': 'adidas'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProductTestCase(TestSetUp):

    def test_product_post(self):
        CategoryTestCase.test_category_post(self)
        data = {
            "name": "Adidas",
            "description": "Best description",
            "price": "4.99",
            "quantity": "2",
            "category": "adidas",
        }

        response = self.client.post(reverse('products'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_get(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('products'),
                                   data={"category": "test"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        Categorie(name='test').save()
        response = self.client.get(reverse('products'),
                                   data={"category": "test"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
