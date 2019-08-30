from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse



def home(request):
    return render(request, 'base.html')
