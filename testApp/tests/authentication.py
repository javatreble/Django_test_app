# Testing authentication
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestDownloadView(TestCase):
    # To test if the "/download/" page accessible to only authenticated users
    def test_anonymous_cannot_see_page(self):
        print('Running test test_anonymous_cannot_see_page() ')
        response = self.client.get(reverse("contacts:download"))
        self.assertRedirects(response, "/accounts/login?next=/download/")

    # To test an authenticated user
    def test_authenticated_user_can_see_page(self):
        print('Running test test_authenticated_user_can_see_page() ')
        # Create the user in the test
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("contacts:download"))
        self.assertEqual(response.status_code, 200)