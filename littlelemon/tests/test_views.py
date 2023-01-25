from django.test import TestCase
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        MenuItem.objects.create(title="Apple", price=5, inventory=10)
    def test_getall(self):
        objects = MenuItem.objects.all()