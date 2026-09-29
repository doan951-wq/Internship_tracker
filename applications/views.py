from django.http import HttpResponse


# A view is a function Django calls to handle a browser request.
# Django supplies the request argument with information about that visit.
def internship_list(request):
    # HttpResponse creates a response containing text for the browser.
    return HttpResponse("Your internship tracker")
