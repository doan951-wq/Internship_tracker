from datetime import date

from django.test import TestCase

from .models import Internship


# Django finds classes that inherit from TestCase and runs their test_ methods.
class InternshipListTests(TestCase):
    def test_homepage_shows_internship_name(self):
        # Make one temporary database row for this test.
        Internship.objects.create(name="Google", apply_by=date(2026, 10, 31))

        # Django's test client acts like a browser visiting the homepage.
        response = self.client.get("/")

        # The test passes only if the page contains this name.
        self.assertContains(response, "Google")


class InternshipCreateTests(TestCase):
    def test_submitting_valid_form_creates_internship(self):
        # Submit the same field values a browser would send from the form.
        response = self.client.post("/new/", {
            "name": "Microsoft",
            "apply_by": "2026-10-31",
            "status": "applied",
        })

        # Check that the form submission saved exactly one row.
        self.assertEqual(Internship.objects.count(), 1)
        internship = Internship.objects.get()
        self.assertEqual(internship.name, "Microsoft")
        self.assertEqual(internship.apply_by, date(2026, 10, 31))
        self.assertEqual(internship.status, "applied")

        # A successful submission sends the browser back to the homepage.
        self.assertRedirects(response, "/")
