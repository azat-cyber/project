from django.shortcuts import render, HttpResponse
from .models import Test

def homepage(request):
    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def contacts(request):
    test_list = Test.objects.all()
    return render(request, "contacts.html", {"test_listUse": test_list})
