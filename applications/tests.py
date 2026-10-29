from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import STATUS_CHOICES, Internship


class AuthenticatedTestCase(TestCase):
    def setUp(self):
        super().setUp()
        user = get_user_model().objects.create_user(username="testuser")
        self.client.force_login(user)


class LoginRequiredTests(TestCase):
    def test_anonymous_requests_redirect_without_changing_internships(self):
        internship = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31)
        )
        urls = ["/", "/new/", f"/{internship.id}/edit/", f"/{internship.id}/delete/"]
        for url in urls:
            for method in ("get", "post"):
                with self.subTest(url=url, method=method):
                    data = {
                        "name": "Changed", "apply_by": "2026-11-01", "status": "offer",
                    } if method == "post" else {}
                    response = getattr(self.client, method)(url, data)
                    self.assertRedirects(response, f"/accounts/login/?next={url}")
                    self.assertEqual(Internship.objects.count(), 1)
                    internship.refresh_from_db()
                    self.assertEqual(internship.name, "Google")
                    self.assertEqual(internship.apply_by, date(2026, 10, 31))
                    self.assertEqual(internship.status, "applied")


# These tests log in before exercising the protected views.
class InternshipListTests(AuthenticatedTestCase):
    def test_homepage_shows_internship_name(self):
        # Make one temporary database row for this test.
        Internship.objects.create(name="Google", apply_by=date(2026, 10, 31))

        # Django's test client acts like a browser visiting the homepage.
        response = self.client.get("/")

        # The test passes only if the page contains this name.
        self.assertContains(response, "Google")

    def test_homepage_orders_internships_by_deadline(self):
        # Create the later deadline first to check that dates control the order.
        later = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31)
        )
        earlier = Internship.objects.create(
            name="Microsoft", apply_by=date(2026, 10, 15)
        )

        response = self.client.get("/")

        # Compare the rows supplied to the template with the expected order.
        self.assertEqual(list(response.context["internships"]), [earlier, later])

    def test_status_filter_shows_only_matching_internships_in_deadline_order(self):
        later = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31), status="interview"
        )
        earlier = Internship.objects.create(
            name="Microsoft", apply_by=date(2026, 10, 15), status="interview"
        )
        Internship.objects.create(
            name="Amazon", apply_by=date(2026, 10, 1), status="applied"
        )

        response = self.client.get("/", {"status": "interview"})

        self.assertEqual(list(response.context["internships"]), [earlier, later])
        self.assertContains(response, "Google")
        self.assertContains(response, "Microsoft")
        self.assertNotContains(response, "Amazon")
        self.assertContains(
            response, '<option value="interview" selected>Interview</option>',
            html=True,
        )

    def test_status_filter_supports_every_status_choice(self):
        for status, label in STATUS_CHOICES:
            Internship.objects.create(
                name=label, apply_by=date(2026, 10, 31), status=status
            )

        for status, label in STATUS_CHOICES:
            with self.subTest(status=status):
                response = self.client.get("/", {"status": status})
                self.assertEqual(
                    list(response.context["internships"].values_list("status", flat=True)),
                    [status],
                )

    def test_status_filter_with_no_matches_shows_empty_message(self):
        Internship.objects.create(name="Google", apply_by=date(2026, 10, 31))

        response = self.client.get("/", {"status": "offer"})

        self.assertEqual(list(response.context["internships"]), [])
        self.assertContains(response, "No internships match this status.")
        self.assertNotContains(response, "No internships yet.")

    def test_all_statuses_and_invalid_status_show_all_internships(self):
        later = Internship.objects.create(
            name="Google", apply_by=date(2026, 10, 31), status="interview"
        )
        earlier = Internship.objects.create(
            name="Microsoft", apply_by=date(2026, 10, 15), status="applied"
        )

        for params in ({}, {"status": ""}, {"status": "unknown"}):
            with self.subTest(params=params):
                response = self.client.get("/", params)
                self.assertEqual(list(response.context["internships"]), [earlier, later])
                self.assertContains(
                    response, '<option value="" selected>All statuses</option>',
                    html=True,
                )


class InternshipCreateTests(AuthenticatedTestCase):
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


class InternshipEditTests(AuthenticatedTestCase):
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


class InternshipDeleteTests(AuthenticatedTestCase):
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
