from django.test import TestCase, Client
from django.urls import reverse
from .models import Comets

class CometsModelTest(TestCase):
    def setUp(self):
        # Create a comet instance for testing
        self.comet = Comets.objects.create(
            name="Halley",
            size=11.0,
            color="White",
            tail=True,
            myprompt="A famous comet"
        )

    def test_comet_creation(self):
        # Verify the comet instance has the expected attribute values
        comet = Comets.objects.get(name="Halley")
        self.assertEqual(comet.name, "Halley")
        self.assertEqual(comet.size, 11.0)
        self.assertEqual(comet.color, "White")
        self.assertTrue(comet.tail)
        self.assertEqual(comet.myprompt, "A famous comet")

class CometsViewsTest(TestCase):
    def setUp(self):
        # Create comet instances and initialize the test client
        self.client = Client()
        self.comet1 = Comets.objects.create(
            name="Halley",
            size=11.0,
            color="White",
            tail=True,
            myprompt="A famous comet"
        )
        self.comet2 = Comets.objects.create(
            name="Hale-Bopp",
            size=40.0,
            color="Blue",
            tail=True,
            myprompt="A large comet"
        )

    def test_index2_view(self):
        # Test the 'index2' view to ensure it returns a 200 status code and contains the comet names
        response = self.client.get(reverse('comet:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comet1.name)
        self.assertContains(response, self.comet2.name)

    def test_comet_details_view(self):
        # Test the 'comet_details' view to ensure it returns a 200 status code and contains the comet attributes
        response = self.client.get(reverse('comet:comet_details', args=[self.comet1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comet1.name)
        self.assertContains(response, self.comet1.color)

    def test_index2_view_with_comet_selection(self):
        # Test the 'index2' view with a specific comet selected to ensure it returns a 200 status code
        response = self.client.get(reverse('comet:index'), {'comet': self.comet1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comet1.name)
        self.assertContains(response, self.comet1.myprompt)
        self.assertContains(response, self.comet2.name)

    def test_index2_view_navigation(self):
        # Test the navigation functionality in the 'index2' view
        response = self.client.get(reverse('comet:index'), {'comet': self.comet1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comet1.name)

        # Find the previous and next comet IDs in the context
        prev_comet_id = self.comet2.id
        next_comet_id = self.comet2.id

        # Check if the response contains the correct IDs for previous and next comets
        self.assertContains(response, f'value="{prev_comet_id}"')
        self.assertContains(response, f'value="{next_comet_id}"')

