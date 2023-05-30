from django.shortcuts import render,redirect
from . models import Subject

# Create your views here.


def index(request):
    sub = Subject.objects.all()
    context = { "sub_list": sub}
    return render(request,"index.html" , context=context)


def add_subject(request):
    if request.method == "POST":
        name = request.POST["name"]
        code = request.POST["code"]
        Subject.objects.create(name=name, code=code)
        return redirect("/")
    return render(request, "add_sub.html")
    