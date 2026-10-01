# Django's forms module contains classes for building and validating forms.
from django import forms

# This is the Internship model class we wrote in this app's models.py file.
from .models import Internship


# ModelForm is a Django parent class that can build a form from a model.
class InternshipForm(forms.ModelForm):
    # Django reads this inner Meta class to learn which model and fields to use.
    class Meta:
        model = Internship
        fields = ["name", "apply_by", "status"]
