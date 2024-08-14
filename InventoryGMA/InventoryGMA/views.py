from django.shortcuts import redirect, render

from .forms import ThingForm, CategoryForm
from .models import Thing, Category

def index(request):
    template = "index.html"
    context = {}
    context["things"] = Thing.objects.all()
    context["categories"] = Category.objects.all()
    return render(request, template, context)


def thingForm_view(request):
    if request.method == "POST":
        form = ThingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save() 
            return redirect("index")
        #Went wrong
        else:
            context = {"error":form.errors}
            return render(request, "error.html", context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ThingForm()
        return render(request, "form.html", {"form": form, "nextStep":"thingForm"})

def categoryForm_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save() 
            return redirect("index")
        #Went wrong
        else:
            context = {"error":form.errors}
            return render(request, "error.html", context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryForm()
        return render(request, "form.html",{"form": form, "nextStep":"categoryForm"})