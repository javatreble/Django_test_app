from django.test import TestCase
from django.urls import reverse

from testApp.models import Contact


class TestStudentContactForm(TestCase):
    # test for the classic POST/Redirect/GET pattern
    def test_can_send_message(self):
        print('Running test_can_send_message()')
        data = { # generate i/p
            "first_name": "Juliana",
            "last_name": " Crain",
            "message": "Would love to talk about Philip K. Dick",
        }

        # with Django test client we send the request.
        response = self.client.post("/contact/", data=data) # send
        # # OR use reverse to check for the URLs by name rather than by path
        # response = self.client.get(reverse("contacts:contact"))
        self.assertEqual(Contact.objects.count(), 1) #temp db

        # check if the view redirected correctly
        self.assertRedirects(response, "/thanks/")
        # # OR use reverse to check for the URLs by name rather than by path
        # response = self.client.get(reverse("contacts:thanks")) #REverse mapping

        response = self.client.get("/contact/")
        self.assertTemplateUsed(response, "contact_form.html")

        # test for appearance two model fields in the HTML
        self.assertContains(response, "first_name") #
        self.assertContains(response, "last_name")
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertRedirects(response, "/thanks/")
