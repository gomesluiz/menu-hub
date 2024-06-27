from django.test import TestCase
from .models import Restaurant


class ShowRestaurantsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.restaurant = Restaurant.objects.create(name="Pizza na Roça")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_model_content(self):
        self.assertEqual(self.restaurant.name, "Pizza na Roça")
