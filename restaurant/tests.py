
# Create your tests here.
from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(
            title="Ice Cream",
            price=100,
            inventory=20
        )

        self.assertEqual(item.title, "Ice Cream")
        self.assertEqual(item.price, 100)