from django.shortcuts import render, HttpResponse
from .models import Test

def homepage(request):
    return render(request, "index.html")


def about(request):
    test_list = Test.objects.all()
    return render(request, "about.html", {"test_listUse": test_list})


def contacts(request):
    return render(request, "contacts.html")
