from django.test import SimpleTestCase
from django.urls import reverse, resolve
from AppLibros.views import *


class TestUrls(SimpleTestCase):
    # def test_list_url_is_resolved(self):
    #     assert 1 == 1

    def test_list_url_is_resolved2(self):
        url = reverse("AppLibros:index")
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_list_url_is_resolved3(self):
        url = reverse("AppLibros:NuevoLibro")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LibroCreateView)

    def test_list_url_is_resolved4(self):
        url = reverse("AppLibros:ListaLibros")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LibroListView)
