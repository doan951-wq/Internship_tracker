# Import Django's database-model tools. The `models` module contains classes
# such as Model, CharField, and DateField.
from django.db import models


# This is a list of tuples. Each tuple contains:
# (the value stored in PostgreSQL, the label shown to the user).
STATUS_CHOICES = [
    ("applied", "Applied"),
    ("oa", "Online assessment"),
    ("phone screen", "Phone screen"),
    ("interview", "Interview"),
    ("offer", "Offer"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
]


# Inheriting from models.Model turns this normal Python class into a Django
# model. Django will connect the model to a PostgreSQL table.
class Internship(models.Model):
    # CharField describes a text column. Each internship object will store its
    # own string in its `name` attribute.
    name = models.CharField(max_length=200)

    # DateField stores a calendar date rather than an unrestricted string.
    apply_by = models.DateField()

    # This is also a text column. `choices` limits the normal options, and
    # `default` is used when no status is supplied.
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied",
    )

    # Python calls __str__ when it needs a readable string for an object.
    # `self` is the particular Internship object being displayed.
    def __str__(self):
        return self.name
