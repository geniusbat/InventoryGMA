from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse

from .forms import ThingForm, CategoryForm, LocationForm
from .models import Thing, Category, Location

def index(request):
    template = "index.html"
    context = {}
    context["things"] = Thing.objects.all()
    context["categories"] = Category.objects.all()
    context["locations"] = Location.objects.all()
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

def thing_delete(request, id):
    template = "index.html"
    ins = get_object_or_404(Thing, pk=id)
    ins.delete()
    return redirect("index")
    

def filterThings_view(request):
    if request.method == "POST":
        post = request.POST
        nameFilter = post["nameFilterInput"].strip()
        descriptionFilter = post["descriptionFilterInput"].strip()
        categoryFilter = []
        if "all" in post.getlist("categoryFilterInput"):
            categoryFilter = "all"
        else:
            for el in post.getlist("categoryFilterInput"):
                if el == "null":
                    categoryFilter.append(None)
                else:
                    categoryFilter.append(int(el))
        locationFilter = []
        if post.getlist("locationFilterInput") != "":
            if "all" in post.getlist("locationFilterInput"):
                locationFilter = "all"
            else:
                for el in post.getlist("locationFilterInput"):
                    if el == "null":
                        locationFilter.append(None)
                    else:
                        locationFilter.append(int(el))
        minNumberFilter = post["minNumberFilterInput"].strip()
        maxNumberFilter = post["maxNumberFilterInput"].strip()
        objs = Thing.objects
        if nameFilter != "":
            objs = objs.filter(name__icontains=nameFilter)
        if descriptionFilter != "":
            objs = objs.filter(description__icontains=descriptionFilter)
        if categoryFilter != "" and categoryFilter != "all":
            if None in categoryFilter:
                from django.db.models import Q
                categoryFilter.remove(None)
                objs = objs.filter((Q(category__isnull=True)))
            if len(categoryFilter)>0:
                objs = objs.filter(category__pk__in=categoryFilter)
        if locationFilter != "" and locationFilter != "all":
            if None in locationFilter:
                from django.db.models import Q
                locationFilter.remove(None)
                objs = objs.filter((Q(location__isnull=True)))
            if len(locationFilter)>0:
                objs = objs.filter(location__in=locationFilter)
        if minNumberFilter != "":
            minNumberFilter = int(minNumberFilter)
            objs = objs.filter(quantity__gte=minNumberFilter)
        if maxNumberFilter != "":
            maxNumberFilter = int(maxNumberFilter)
            if minNumberFilter == "" or maxNumberFilter>minNumberFilter:
                objs = objs.filter(quantity__lte=maxNumberFilter)
        context = {}
        context["things"] = objs.all()
        context["categories"] = Category.objects.all()
        context["locations"] = Location.objects.all()
        template = "index.html"
        return render(request, template, context)
    else:
        redirect("index")

def UpdateForm(request, what, id):
    if request.method == "POST":
        print(id)
        form = None
        if what == "thing":
            ins = get_object_or_404(Thing, pk=id)
            form = ThingForm(request.POST, instance=ins)
        elif what == "category":
            ins = get_object_or_404(Category, pk=id)
            form = CategoryForm(request.POST, instance=ins)
        elif what == "location":
            ins = get_object_or_404(Location, pk=id)
            form = LocationForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = None
        nextStep = None
        if what == "thing":
            form = ThingForm(instance=get_object_or_404(Thing, pk=id))
            nextStep = "thingForm"
        elif what == "category":
            form = CategoryForm(instance=get_object_or_404(Category, pk=id))
            nextStep = "categoryForm"
        elif what == "location":
            form = LocationForm(instance=get_object_or_404(Location, pk=id))
            nextStep = "locationForm"
        aux = reverse("updateForm", args=[what,id])
        return render(request, "form.html",{"form": form, "rawUrl":aux})
        

def category_view(request):
    template = "view_categories.html"
    context = {}
    context["categories"] = Category.objects.all()
    return render(request, template, context)

def category_create(request):
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

def category_delete(request, id):
    template = "view_categories.html"
    ins = get_object_or_404(Category, pk=id)
    ins.delete()
    return redirect("categoryView")


def location_view(request):
    template = "view_locations.html"
    context = {}
    context["locations"] = Location.objects.all()
    return render(request, template, context)

def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
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
        form = LocationForm()
        return render(request, "form.html",{"form": form, "nextStep":"locationForm"})

def location_delete(request, id):
    template = "view_locations.html"
    ins = get_object_or_404(Location, pk=id)
    ins.delete()
    return redirect("locationView")