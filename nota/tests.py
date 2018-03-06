from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .serializers import NotaSerializer
from .models import Nota


class AccountTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="usuario_teste", password="usuario_teste"
        )
        self.note = Nota.objects.create(
            titulo="Note Usuario", texto="Note Usuario",
            autor=self.user
        )
        self.other_user = User.objects.create_user(
            username="usuario_outro", password="usuario_outro"
        )
        self.note_other_user = Nota.objects.create(
            titulo="Outro Usuario", texto="Outro Usuario",
            autor=self.other_user
        )
        self.data_base = {
            "titulo": "titulo",
            "texto": "texto"
        }

    def test_notes_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/notas/")
        note_serialized = NotaSerializer(self.note).data
        self.assertIn(note_serialized, response.json())

    def test_create_not_logged(self):
        response = self.client.post("/api/notas/", data=self.data_base)
        self.assertEqual(response.status_code, 403)

    def test_create_logged(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/notas/", data=self.data_base)
        self.assertEqual(response.status_code, 201)

    def test_blank(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/api/notas/", data={"titulo": "", "texto": ""}
        )
        self.assertEqual(response.status_code, 400)

    def test_no_data(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/notas/")
        self.assertEqual(response.status_code, 400)

    def test_note_other_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/notas/")
        self.assertNotIn(self.note_other_user, response.data)

    def test_note_other_user_by_id(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/notas/{id}/".format(
            id=self.note_other_user.id
        ))
        self.assertEqual(response.status_code, 404)

    def test_edit_note(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            "/api/notas/{id}/".format(id=self.note.id),
            data={
                "titulo": "MUDEI O TITULOOOOOO",
                "texto": "aklsdjklasjdlkasjdlkasd asdhalskd"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.titulo, "MUDEI O TITULOOOOOO")
