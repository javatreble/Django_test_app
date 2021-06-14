from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from testApp.models import Contact


class ContactCreate(CreateView): #GET POST
    model = Contact
    fields = ["first_name", "last_name", "message"]
    template_name = 'contact_form.html'
    success_url = reverse_lazy("contacts:thanks") #


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")

@login_required
def download(request):
    return HttpResponse("Download will start soon. Thank you!")