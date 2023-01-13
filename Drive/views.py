from django.shortcuts import render
from .models import *
def Home(r):
    return render(r,'index.html',{"posts":Post.objects.all(),"interns":Intern.objects.all()})
def View(r):
    return render(r,"View.html")
def Form(r):
    return render(r,"form.html")
def Course(r):
    return render(r,"Course.html",{"posts":Post.objects.all()})
def Online(r):
    return render(r,"Onlinpayment.html")