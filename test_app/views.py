from django.shortcuts import render, HttpResponse, redirect
from .models import Test

def homepage(request):
    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def contacts(request):
    test_list = Test.objects.all()
    return render(request, "contacts.html", {"test_listUse": test_list})

def add_todo(request):
    form = request.POST
    text = form["text_todo"]
    todo = Test(text=text)
    todo.save()
    return redirect(contacts)
