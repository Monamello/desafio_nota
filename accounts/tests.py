from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class AccountTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="usuario_teste", password="usuario_teste"
        )
        self.data_base = {
            "first_name": "Teste",
            "last_name": "Teste",
            "email": "teste@teste.com",
            "username": "teste",
            "password": "teste"
        }

    def test_create_new_user(self):
        response = self.client.post("/api/accounts/", data=self.data_base)
        self.assertEqual(response.status_code, 201)
        has_user = User.objects.filter(username="teste").exists()
        self.assertTrue(has_user)

    def test_create_if_logged(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/accounts/", data=self.data_base)
        self.assertEqual(response.status_code, 403)

    def test_create_existed_user(self):
        data = {
            "username": "usuario_teste",
            "password": "usuario_teste"
        }
        response = self.client.post("/api/accounts/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content.decode(),
            {'username': ['A user with that username already exists.']}
        )

    def test_create_no_data(self):
        response = self.client.post("/api/accounts/")
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content.decode(),
            {
                'password': ['This field is required.'],
                'username': ['This field is required.']
            }
        )

    def test_user_created_is_superuser(self):
        data = {
            "username": "usuario_nao_admin",
            "password": "usuario_nao_admin"
        }
        response = self.client.post("/api/accounts/", data=data)
        self.assertEqual(response.status_code, 201)
        user = User.objects.filter(username="usuario_nao_admin").first()
        self.assertFalse(user.is_superuser)
