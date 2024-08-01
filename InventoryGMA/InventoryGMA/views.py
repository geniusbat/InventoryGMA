from django.shortcuts import redirect, render

def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)