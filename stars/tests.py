# stars/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Stars

class StarsModelTest(TestCase):
    def setUp(self):
        # Create a star instance for testing
        self.star = Stars.objects.create(
            name="Sun",
            size="Large",
            color="Yellow",
            temperature=5778,
            myprompt="A yellow star"
        )

    def test_star_creation(self):
        # Verify the star instance has the expected attribute values
        star = Stars.objects.get(name="Sun")
        self.assertEqual(star.name, "Sun")
        self.assertEqual(star.size, "Large")
        self.assertEqual(star.color, "Yellow")
        self.assertEqual(star.temperature, 5778)
        self.assertEqual(star.myprompt, "A yellow star")

class StarsViewsTest(TestCase):
    def setUp(self):
        # Create star instances and initialize the test client
        self.client = Client()
        self.star1 = Stars.objects.create(
            name="Sun",
            size="Large",
            color="Yellow",
            temperature=5778,
            myprompt="A yellow star"
        )
        self.star2 = Stars.objects.create(
            name="Sirius",
            size="Large",
            color="White",
            temperature=9940,
            myprompt="A white star"
        )

    def test_index2_view(self):
        # Test the 'index2' view to ensure it returns a 200 status code and contains the star names
        response = self.client.get(reverse('stars:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.star1.name)
        self.assertContains(response, self.star2.name)

    def test_star_details_view(self):
        # Test the 'star_details' view to ensure it returns a 200 status code and contains the star attributes
        response = self.client.get(reverse('stars:star_details', args=[self.star1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.star1.name)
        self.assertContains(response, self.star1.color)

    def test_index2_view_with_star_selection(self):
        # Test the 'index2' view with a specific star selected to ensure it returns a 200 status code
        response = self.client.get(reverse('stars:index'), {'star': self.star1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.star1.name)
        self.assertContains(response, self.star1.myprompt)
        self.assertContains(response, self.star2.name)

    def test_index2_view_navigation(self):
        # Test the navigation functionality in the 'index2' view
        response = self.client.get(reverse('stars:index'), {'star': self.star1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.star1.name)

        # Find the previous and next star IDs in the context
        prev_star_id = self.star2.id
        next_star_id = self.star2.id

        # Check if the response contains the correct IDs for previous and next stars
        self.assertContains(response, f'value="{prev_star_id}"')
        self.assertContains(response, f'value="{next_star_id}"')
