# Django provides render() for HTML pages and redirect() to send the browser
# to another URL after a successful form submission.
from django.shortcuts import redirect, render

# Import the form class we wrote in this app's forms.py file.
from .forms import InternshipForm

# Import our Internship model class from this app's models.py file.
from .models import Internship


# A view is a function Django calls to handle a browser request.
# Django supplies the request argument with information about that visit.
def internship_list(request):
    # Django's manager retrieves the records as a collection of model objects.
    internships = Internship.objects.all()

    # A context dictionary makes Python values available in the HTML template.
    # The key "internships" is the name the template will use for this collection.
    context = {"internships": internships}

    # Django searches the installed apps' templates folders for this file.
    return render(request, "applications/internship_list.html", context)


def internship_new(request):
    if request.method == "POST":
        # request.POST holds the values the browser submitted.
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # A GET request displays an empty form.
        form = InternshipForm()

    # An invalid POST shows the same form again with validation errors.
    context = {"form": form}
    return render(request, "applications/internship_new.html", context)
