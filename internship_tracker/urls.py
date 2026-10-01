"""
URL configuration for internship_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Import the function we wrote in applications/views.py.
from applications.views import internship_edit, internship_list, internship_new

# Django reads this list to choose a view for each requested address.
urlpatterns = [
    # An empty route matches the homepage (/). Django calls this view for us.
    path('', internship_list),
    path('new/', internship_new),
    # Django converts the number in the URL into the internship_id argument.
    path('<int:internship_id>/edit/', internship_edit),
    path('admin/', admin.site.urls),
]
