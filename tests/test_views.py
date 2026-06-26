from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=250, inventory=10)
        Menu.objects.create(title="Burger", price=150, inventory=20)

    def test_getall(self):
        client = APIClient()
        response = client.get("/restaurant/menu/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)