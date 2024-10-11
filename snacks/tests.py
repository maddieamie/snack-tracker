from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model

class SnackTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username="tester", password="pass")
        Snack.objects.create(name="Chips", purchaser=user, description="Salty snack.")

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_view(self):
        snack = Snack.objects.get(name="Chips")
        response = self.client.get(reverse('snack_detail', args=[snack.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')
