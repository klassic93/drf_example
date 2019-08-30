from django.test import override_settings

from rest_framework.test import APITestCase
from rest_framework import status


class CustomUserTestAPI(APITestCase):

    @override_settings(DEBUG=True)
    def test_create_user(self):
        response = self.client.post('/api/v1/users/', {'username':'Tomas'}, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    @override_settings(DEBUG=True)
    def test_get_users(self):
        self.client.post('/api/v1/users/', {'username': 'Tomas'})
        self.client.post('/api/v1/users/', {'username': 'Dima'})

        response = self.client.get('/api/v1/users/')
        self.assertEqual(len(response.data), 2)

    @override_settings(DEBUG=True)
    def test_personaly_user(self):
        user = self.client.post('/api/v1/users/', {'username': 'Tomas'})
        id = user.data.get('id')

        response = self.client.get('/api/v1/users/{}/'.format(id))
        self.assertEqual(response.data.get('username'), 'Tomas')

        response = self.client.patch('/api/v1/users/{}/'.format(id), {'username':'Dima'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('username'), 'Dima')

    @override_settings(DEBUG=True)
    def test_create_book(self):
        user = self.client.post('/api/v1/users/', {'username': 'Tomas'})
        response = self.client.post('/api/v1/books/', {'name':'GarryPotter and somthing',
                                                       'popularity':1,
                                                       'user':user.data.get('id')})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/api/v1/books/', {'name':'GarryPotter and somthing',
                                                       'popularity':1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/api/v1/books/', {'name': 'GarryPotter and somthing else',
                                                       'popularity': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.patch('/api/v1/books/{}/'.format(response.data.get('id')), {
                                                        'name': 'GarryPotter and somthing else',
                                                        'popularity': 1,
                                                        'user':user.data.get('id')})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1/books/{}/'.format(response.data.get('id')))
        self.assertEqual(response.data.get('user'), user.data.get('id'))
