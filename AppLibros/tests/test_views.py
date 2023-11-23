from django.test import TestCase, Client
from django.urls import reverse, resolve
from AppLibros.models import Libro
import json


class TestViews(TestCase):
    def test_Libro_index_get(self):
        client = Client()
        response = client.get(reverse("AppLibros:index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
