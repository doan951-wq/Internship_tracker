# Django provides render() for HTML pages and redirect() to send the browser
# to another URL after a successful form submission.
from django.shortcuts import get_object_or_404, redirect, render

# Import the form class we wrote in this app's forms.py file.
from .forms import InternshipForm

# Import our Internship model class from this app's models.py file.
from .models import STATUS_CHOICES, Internship

from django.contrib.auth.decorators import login_required

# A view is a function Django calls to handle a browser request.
# Django supplies the request argument with information about that visit.
@login_required
def internship_list(request):
    # Retrieve all internships with the earliest application deadlines first.
    internships = Internship.objects.order_by("apply_by")

    # GET parameters let the filter be bookmarked or shared in the page URL.
    search_query = request.GET.get("q", "")
    if search_query:
        internships = internships.filter(name__icontains=search_query)

    selected_status = request.GET.get("status", "")
    if selected_status in dict(STATUS_CHOICES):
        internships = internships.filter(status=selected_status)
    else:
        selected_status = ""

    # A context dictionary makes Python values available in the HTML template.
    # The key "internships" is the name the template will use for this collection.
    context = {
        "internships": internships,
        "status_choices": STATUS_CHOICES,
        "selected_status": selected_status,
        "search_query": search_query
    }

    # Django searches the installed apps' templates folders for this file.
    return render(request, "applications/internship_list.html", context)

@login_required
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

@login_required
def internship_edit(request, internship_id):
    # Find the row named by the URL, or show a 404 page if it does not exist.
    internship = get_object_or_404(Internship, id=internship_id)
    if request.method == "POST":
        # instance= makes save() update this row instead of creating a new one.
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # On GET, instance= fills the fields with this row's current values.
        form = InternshipForm(instance=internship)

    context = {"form": form, "internship": internship}
    return render(request, "applications/internship_edit.html", context)

@login_required
def internship_delete(request, internship_id):
    # Use the number in the URL to find the internship being deleted.
    internship = get_object_or_404(Internship, id=internship_id)

    # Only a submitted form (POST) deletes the row. Visiting the page (GET)
    # merely shows a confirmation question.
    if request.method == "POST":
        internship.delete()
        return redirect("/")

    context = {"internship": internship}
    return render(request, "applications/internship_delete.html", context)
