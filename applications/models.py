from django.db import models


STATUS_CHOICES = [
    ("applied", "Applied"),
    ("oa", "Online assessment"),
    ("phone screen", "Phone screen"),
    ("interview", "Interview"),
    ("offer", "Offer"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
]


class Internship(models.Model):
    name = models.CharField(max_length=200)
    apply_by = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied",
    )

    def __str__(self):
        return self.name
