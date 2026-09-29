# Django provides render() to load an HTML template and return a response.
from django.shortcuts import render

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
