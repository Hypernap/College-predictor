from urllib.request import HTTPRedirectHandler 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Collagename
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect




def home(request):    
    return render(request, 'home1.html')

def main(request):
    context={'clgs':Collagename.objects.all()}
    return render(request,"mainpage.html",context)

def add(request):
    if request.user.is_superuser:
        return HttpResponse("Only admin acccess")
    else:
        return redirect('home1')