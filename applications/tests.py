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

    def test_submitting_blank_name_does_not_create_internship(self):
        # Leave the name empty while submitting valid values for other fields.
        response = self.client.post("/new/", {
            "name": "",
            "apply_by": "2026-10-31",
            "status": "applied",
        })

        # The view displays the form again without saving a row.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Internship.objects.count(), 0)

        # Check that the form explains why the name was rejected.
        self.assertFormError(
            response.context["form"], "name", "This field is required."
        )


class InternshipEditTests(TestCase):
    def test_submitting_edit_form_updates_existing_internship(self):
        # Create the row that the edit form should update.
        internship = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31)
        )

        # Use this row's ID to submit its edit form.
        response = self.client.post(f"/{internship.id}/edit/", {
            "name": "Microsoft",
            "apply_by": "2026-10-31",
            "status": "applied",
        })

        # Reload this Python object's values after the view changes the row.
        internship.refresh_from_db()
        self.assertEqual(internship.name, "Microsoft")
        self.assertEqual(Internship.objects.count(), 1)
        self.assertRedirects(response, "/")

    def test_editing_missing_internship_returns_404(self):
        # This test creates no rows, so internship ID 1 does not exist.
        response = self.client.get("/1/edit/")

        self.assertEqual(response.status_code, 404)


class InternshipDeleteTests(TestCase):
    def test_visiting_delete_page_keeps_internship(self):
        # Create an internship to show on the confirmation page.
        internship = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31)
        )

        # Visiting the page should ask for confirmation without deleting.
        response = self.client.get(f"/{internship.id}/delete/")

        self.assertContains(response, "Delete Google?")
        self.assertTrue(Internship.objects.filter(id=internship.id).exists())

    def test_confirming_delete_removes_internship(self):
        # Create the internship that we will confirm deleting.
        internship = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31)
        )

        # Submit the confirmation form for this internship.
        response = self.client.post(f"/{internship.id}/delete/")

        # The row should be gone, and the browser should return home.
        self.assertFalse(Internship.objects.filter(id=internship.id).exists())
        self.assertRedirects(response, "/")

    def test_deleting_missing_internship_returns_404(self):
        # No internship exists in this test's isolated database data.
        response = self.client.post("/1/delete/")

        self.assertEqual(response.status_code, 404)
