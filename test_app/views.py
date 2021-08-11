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

def delete_todo(request, id):
    todo = Test.objects.get(id=id)
    todo.delete()
    return redirect(contacts)

def mark_todo(request, id):
    todo = Test.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(contacts)

def unmark_todo(request, id):
    todo = Test.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(contacts)

def close_todo(request, id):
    todo = Test.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(contacts)
