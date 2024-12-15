from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import Users


# Create your tests here.
class UsersTestCase(APITestCase):
    """ Тестирование CRUD """

    def setUp(self):
        self.user = Users.objects.create(
            email='test@mail.ru', tg_chat_id='743470705'
        )
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        url = reverse('users:user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        url = reverse('users:user_update', args=(self.user.pk,))
        data = {
            'phone': '+7 777 777 7777',
            'tg_chat_id': '743470706',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('phone'), '+7 777 777 7777')

    def test_user_create(self):
        url = reverse('users:register')
        data = {
            'email': 'test@mail.ru',
            'password': "123qwe",
            'city' : 'test',
            'phone': '+7 777 777 7777',
            'tg_chat_id': '743470705',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.all().count(), 2)

    def test_user_delete(self):
        url = reverse('users:user_delete', args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Users.objects.all().count(), 0)

    def test_user_retrieve(self):
        url = reverse('users:user_viewing', args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('tg_chat_id'), self.user.tg_chat_id)
